import asyncio
from random import choice, randint
from typing import List, Dict
from cron_job import scrape_data
from database.db import FoodDatabase

def parse_events(events: List[Dict]) -> str:
    output = ""
    for index, event in enumerate(events):
        event_str = f"## Event {index+1} \n > **Name**: {event[0]}\n > **Location**: {event[4]}\n > **Time**: {event[3]}\n"
        output += str(event_str)
    return output

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered[0] != "!":
        return None
    lowered = lowered[1:]
    if lowered == '':
        return 'Well, you\'re silent...'
    elif lowered.startswith('hello'):
        return 'Hello there!'
    elif lowered.startswith('good'):
        return 'Good, thanks!'
    elif lowered.startswith('bye'):
        return 'See you!'
    elif lowered.startswith('dice'):
        return f'You rolled: {randint(1,6)}'
    elif lowered.startswith('events --user admin --pass admin'):
        scrape_data()
        return "I am scraping some events and adding them to the database"
    
    elif lowered.startswith('events'):
        """
        return every row in database as event as a joined string
        """
        #datetime 
        scrape_data()
        db = FoodDatabase()
        data = db.get_today_event()
        print("Data from database:", data)
        # print("Data from database:", data)
        output = ""

        if not data:
            return "No events found in database, check back after 12AM or 12PM"
        output = parse_events(data)
        print("parsed output:", output)

        return output if output else "Something went wrong when collecting events, please try again later"
    elif lowered.startswith('help'):
        return """!hello: Say hello to users \n !good: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])

if __name__ == "__main__":
    cmd = '!events'
    output = get_response(cmd)
    print(output)
