import discord
from discord.ext import commands
from typing import List, Dict, Tuple

class PaginationView(discord.ui.View):
    def __init__(self, count: int = 5, data: List[Tuple] = None):
        super().__init__()
        self.current_page = 0
        self.count = count
        self.data = data if data is not None else []

    def create_embed(self, data: List[Tuple]):
        embed = discord.Embed(title=f"🍽️ Event list {self.current_page + 1} / {int(len(self.data) / self.count) + 1} 🍽️")
        
        for event in data:
            value = f"> **Name**: {event[0]}\n > **Location**: {event[4]}\n > **Time**: {event[3]}\n"
            embed.add_field(name=event[0], value=value, inline=False)
        return embed

    async def send(self, ctx):
        self.message = await ctx.send(embed=self.create_embed(self.get_current_page_data()), view=self)

    async def update_message(self, data: List[Tuple]):
        self.update_buttons()
        await self.message.edit(embed=self.create_embed(data), view=self)

    def update_buttons(self):
        if self.current_page == 0:
            self.first_page_button.disabled = True
            self.prev_button.disabled = True
            self.first_page_button.style = discord.ButtonStyle.gray
            self.prev_button.style = discord.ButtonStyle.gray
        else:
            self.first_page_button.disabled = False
            self.prev_button.disabled = False
            self.first_page_button.style = discord.ButtonStyle.green
            self.prev_button.style = discord.ButtonStyle.primary

        if self.current_page == (len(self.data) // self.count):
            self.next_button.disabled = True
            self.last_page_button.disabled = True
            self.next_button.style = discord.ButtonStyle.gray
            self.last_page_button.style = discord.ButtonStyle.gray
        else:
            self.next_button.disabled = False
            self.last_page_button.disabled = False
            self.next_button.style = discord.ButtonStyle.primary
            self.last_page_button.style = discord.ButtonStyle.green

    def get_current_page_data(self):
        right_index = (self.current_page + 1) * self.count
        left_index = self.current_page * self.count
        return self.data[left_index:right_index]

    @discord.ui.button(label="|<", style=discord.ButtonStyle.green)
    async def first_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = 0
        await self.update_message(self.get_current_page_data())
        await interaction.response.defer()

    @discord.ui.button(label="<", style=discord.ButtonStyle.primary)
    async def prev_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = max(0, self.current_page - 1)
        await self.update_message(self.get_current_page_data())
        await interaction.response.defer()

    @discord.ui.button(label=">", style=discord.ButtonStyle.primary)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = min(len(self.data) // self.count, self.current_page + 1)
        await self.update_message(self.get_current_page_data())
        await interaction.response.defer()

    @discord.ui.button(label=">|", style=discord.ButtonStyle.green)
    async def last_page_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.current_page = len(self.data) // self.count
        await self.update_message(self.get_current_page_data())
        await interaction.response.defer()
