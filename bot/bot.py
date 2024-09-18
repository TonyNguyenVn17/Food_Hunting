from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message 
from responses import get_response
from discord.ext import tasks, commands # task is used to schedule a function to run at a specific time
from datetime import datetime, timedelta
from cron_job import scrape_by_time
import threading
import asyncio
from pagination import PaginationView
from database.db import FoodDatabase
from cron_job import scrape_data
from collections import defaultdict
from datetime import datetime

#! LOAD OUR TOKEN FROM SOMEWHERE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')
RETRY = 5
#! BOT SETUP
"""
    * Create a bot instance 
        Activate the intents - permission the bot need
        to be able to see the message and respond
    
    """
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents) # intents from client
user_cooldown = {}
COOLDOWN_PERIOD = 30

# ! SEE IF WHETHER USER IS SENDING MESSAGE TOO QUICKLY OR NOT
async def debounce_message(message: Message):
    user_id = message.author.id
    current_time = datetime.now()
    
    if user_id in user_cooldown:
        last_message_time = user_cooldown[user_id]
        if (current_time - last_message_time).seconds < 30:
            print(f"period {(current_time - last_message_time).seconds}")
            return True
    
    user_cooldown[user_id] = current_time
    return False
    
        
#! MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    #* None because it's only meant to execute code
    
    # Check if there is a message
    if not user_message:
        print(' Message was empty because intents were not enabled probably')
        return
    
    # Bot message back privately
    if is_private := user_message[0] == '?':
        # '?' used to indicate private message that user can trigger bot to send private message
        user_message = user_message[1:] # slice the message not include ?
    
    try:
        response : str = get_response(user_message)
        if response is None:
            return
        # if private is said to true, send the message privately
        # otherwise send to the current channel
        await message.author.send(response) if is_private else await message.channel.send(response)
  
    except Exception  as e:
        print(e)  # Reschedule for next Saturday
  
    
#! START BOT MESSAGE
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # friday_10pm_task.start()
    # saturday_11am_task.start()
    guild = client.get_guild(SERVER_ID)  
    if guild is not None:
        channel = guild.get_channel(CHANNEL_ID) 
        if channel is not None:
            await channel.send("Hello What's Up Baby I am back")

#! HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user: # this means bot is the who wrote the message
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'{username} said {user_message} in {channel}')
    print(f'Processing message: {user_message}')  
    
    if message and message[0] == "!" and await debounce_message(message):
        await message.channel.send(f"You're sending messages too quickly. Please wait {COOLDOWN_PERIOD} seconds.")
        return 
    
    if user_message == "!events":
        db = FoodDatabase()
        data = db.get_today_event()
        count = 0
        while not data and count < RETRY:
            print(f"no data in database, scraping attemp {count}")
            scrape_data()
            data = db.get_today_event()
            count += 1
        pagination_view = PaginationView(count=5, data=data)
        await pagination_view.send(message.channel)
    else:       
        await send_message(message, user_message)
        
#! MAIN ENTRY POINT
def run() -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        client.run(token = TOKEN)
    except Exception as e:
        print('Got some Error:', str(e))

if __name__ == '__main__':
    bot_thread = threading.Thread(target=run)
    bot_thread.start()
    scrape_by_time()
