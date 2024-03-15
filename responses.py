import asyncio
import concurrent.futures
from random import choice, randint
from typing import List, Dict
from get_food_event import check_login, open_food_page, find_events
from db import FoodDatabase


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    if lowered[0] != "!":
        return None
    lowered = lowered[1:]

    if lowered.startswith('events --user admin --pass admin'):
        loop = asyncio.get_event_loop()
        loop.run_in_executor(concurrent.futures.ThreadPoolExecutor(), scrape_data)
        return "I am scraping some events and adding them to database"

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
    elif lowered.startswith('events'):
        """
        return every row in database as event as a joined string
        """
        # data = scrape_data() return data directly from bullsconnect
        # return event from database
        db = FoodDatabase()
        # TODO: Replace with today's event
        data = db.get_all_event()
        output = ""

        if not data:
            return "No events found in database, check back after 12AM or 12PM"

        for index, event in enumerate(data):
            event_str = f"## Event {index+1} \n > **Name**: {event[0]}\n > **Location**: {event[4]}\n > **Time**: {event[3]}\n"
            output += str(event_str)

        return output
    elif lowered.startswith('help'):
        return """!hello: Say hello to users \n !good: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])


def scrape_data() -> Dict[str, List[Dict[str, str]]]:

    # TODO: Implement this function
    """
    scrape at 12AM and 12PM daily
    then add data to db
    """
    db = FoodDatabase()
    check_login()
    open_food_page()
    events = find_events()
    for event in events:
        db.add_event(event)


if __name__ == "__main__":
    cmd = '!events'
    output = get_response(cmd)
    print(output)
