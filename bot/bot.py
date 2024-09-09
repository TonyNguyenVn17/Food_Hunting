from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message 
from responses import get_response
from discord.ext import tasks # task is used to schedule a function to run at a specific time
from datetime import datetime, timedelta
from cron_job import scrape_by_time
import threading
import asyncio

#! LOAD OUR TOKEN FROM SOMEWHERE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
SERVER_ID = os.getenv('SERVER_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')

#! BOT SETUP
"""
    * Create a bot instance 
        Activate the intents - permission the bot need
        to be able to see the message and respond
    
    """
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents) # intents from client

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
        await message.author.send(response) if is_private else await message.channel.send(response)
        # if private is said to true, send the message privately
        # otherwise send to the current channel
        
    except Exception  as e:
        print(e)

def seconds_until_friday_10pm():
    now = datetime.now()
    next_friday_10pm = (now + timedelta((4 - now.weekday() + 7) % 7)).replace(hour=22, minute=0, second=0, microsecond=0)
    seconds = (next_friday_10pm - now).total_seconds()
    return seconds if seconds >= 0 else seconds + 604800

def seconds_until_saturday_11am():
    now = datetime.now()
    next_saturday_11am = (now + timedelta((5 - now.weekday() + 7) % 7)).replace(hour=11, minute=0, second=0, microsecond=0)
    seconds = (next_saturday_11am - now).total_seconds()
    return seconds if seconds >= 0 else seconds + 604800

#TODO: Fix this bug on channel not found
# @tasks.loop(seconds=seconds_until_friday_10pm())
# async def friday_10pm_task():
#     channel = client.get_channel(CHANNEL_ID)
#     await channel.send("12PM - ISA - PROJECT TIME - ATTANDANCE MANDATORY")
#     friday_10pm_task.change_interval(seconds=seconds_until_friday_10pm())  # Reschedule for next Friday

#TODO: Fix this bug on channel not found
# @tasks.loop(seconds=seconds_until_saturday_11am())
# async def saturday_11am_task():
#     channel = client.get_channel(CHANNEL_ID)
#     await channel.send("REMINDER - 12PM - ISA - PROJECT TIME - ATTANDANCE MANDATORY")
#     saturday_11am_task.change_interval(seconds=seconds_until_saturday_11am())  # Reschedule for next Saturday
  
    
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
    await send_message(message, user_message) # send the message to the send_message function
        
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
