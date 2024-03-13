from random import choice, randint
from typing import List, Dict
# from get_food_event import check_login, open_food_page, find_events
from db import FoodDatabase


def get_response(user_input : str) -> str:
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
    elif lowered.startswith('events'):
        """
        return every row in database as event as a joined string
        """
        # data = scrape_data() return data directly from bullsconnect
        # return event from database
        db = FoodDatabase()
        data = db.get_all_event()
        output = ""
        for index, event in enumerate(data):
            event_str = f"## Event {index+1} \n > **Name**: {event[0]}\n > **Location**: {event[4]}\n > **Time**: {event[3]}\n"
            output += str(event_str)
            
        
        # for name,event_list in data.items():
        #     for event in event_list:
        #         events.append(event)
        #         names.append(name)
        # formatted_events = []
        # for i in range(len(events[:10])):
        #     one_event = f"Event {i+1}: {names[i]} \nLocation: {events[i]['location']} \nTime: {events[i]['time']}\n"
        #     formatted_events.append(one_event)
        return output
    elif lowered.startswith('help'):
        return """!hello: Say hello to users \n good?: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
    

#def generate_data(name, time, location, URL):
    ##   'name': name,
     #   'time': time,
     #   'location': location,
     #   'URL': URL
   # }


def scrape_data() -> Dict[str, List[Dict[str, str]]]:
    """
    run at 12AM daily
    add data to db
    """
    db = FoodDatabase()
    check_login()
    open_food_page()
    events = find_events()
    data = {}
    for event in events:
        event_name = event['name']
        data[event_name] = [{
            "id": event['id'],
            "tags": event['tags'],
            "date": event['date'],
            "time": event['time'],
            "location": event['location']
        }]
        db.add_event(event)
         

if __name__ == "__main__":
    cmd='!events'
    output=get_response(cmd)
    print(output)
    
