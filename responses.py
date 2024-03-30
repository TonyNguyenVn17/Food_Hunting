import asyncio
from random import choice, randint
from typing import List, Dict
# from cron_job import scrape_data
from db import FoodDatabase
import discord
import datetime
import discord

def get_embed_list(event_list : list):
    embeds = []
    if event_list is None or len(event_list) == 0:
        return embeds

    DATE_STAMP = datetime.datetime.now()
    

    for index, event in enumerate(event_list):
        embed = {}

        embed["title"]       = f"{index+1}. {event[0]}"
        embed["description"] = f"**Location**: {event[4]}\n**Time**:{event[3]}\n",
        embed["color"]       = 2346475
        embed["fields"]      = []
        embed["footer"]      = { "text" : "FeedMe"}
        embed["timestamp"]   = DATE_STAMP

        embeds.append(embed)
    
    return embeds

def get_response(user_input: str) -> dict:
    output = {}
    content = ""
    embeds = []
    
    lowered: str = user_input.lower()
    if lowered[0] != "!":
        return None
    lowered = lowered[1:]
    if lowered == '':
        content =  'Well, you\'re silent...'
    elif lowered.startswith('hello'):
        content =  'Hello there!'
    elif lowered.startswith('good'):
        content =  'Good, thanks!'
    elif lowered.startswith('bye'):
        content =  'See you!'
    elif lowered.startswith('dice'):
        content =  f'You rolled: {randint(1,6)}'
    elif lowered.startswith('events --user admin --pass admin'):
        scrape_data()
        channel.send("I am scraping some events and adding them to the database")
    elif lowered.startswith('events'):
        """
        return every event in table as a list of dict
        """

        db = FoodDatabase()
        data = db.get_today_event()
        content = "**Here's the full list of today's food events. Enjoy!** 🍽️"

        if not data:
            content = "No events found in database, check back after 12AM or 12PM"

        embeds = get_embed_list(data)
        # for index, event in enumerate(data):
        #     event_str = f"## Event {index+1} \n > **Name**: {event[0]}\n > **Location**: {event[4]}\n > **Time**: {event[3]}\n"
        #     output += str(event_str)
        

    elif lowered.startswith('help'):
        content = """!hello: Say hello to users \n !good: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    
    else:
        content =  choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])

    output["content"] = content
    output["embeds"]  = embeds

    return output
    
if __name__ == "__main__":
    cmd = '!events'
    # output = get_response(cmd)
    # print(output)
