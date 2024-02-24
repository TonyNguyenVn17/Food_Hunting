from random import choice, randint
from typing import List, Dict

def get_response(user_input : str) -> str:
    lowered: str = user_input.lower()
    if lowered[0] != "!":
        return None
    lowered = lowered[1:]
    if lowered == '':
        return 'Well, you\'re silent...'
    elif lowered.startswith('hello'):
        return 'Hello there!'
    elif lowered.startswith('good?'):
        return 'Good, thanks!'
    elif lowered.startswith('bye'):
        return 'See you!'
    elif lowered.startswith('dice'):
        return f'You rolled: {randint(1,6)}'
    elif lowered.startswith('events'):
        data = get_data()
        events = []
        for event_list in data.values():
            for event in event_list:
                events.append(event)
        formatted_events = []
        for i in range(len(events)):
            one_event = f"Event{i+1}: {events[i]['name']} \n Location: {events[i]['location']} \n Time: {events[i]['time']} \n URL: {events[i]['URL']}\n"
            formatted_events.append(one_event)
        return '\n'.join(formatted_events)
    elif lowered.startswith('help'):
        return """!hello: Say hello to users \n good?: My feeling now \n !bye: Say goodbye to Bot \n !dice: How lucky are you today \n !events: List of food events today \n !help: Showing this lists"""
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])
    

def generate_data(name, time, location, URL):
    return {
        'name': name,
        'time': time,
        'location': location,
        'URL': URL
    }


def get_data() -> dict[str, List[Dict[str, str]]]:
    data = {}
    for i in range(1, 11):
        event_name = f'event{i}'
        data[event_name] = [generate_data(
            name=event_name,
            time=f'{i} pm',
            location=f'ENB {i}',
            URL=f'https://example.com/events/{event_name}'
        )]
    return data

if __name__ == "__main__":
    data = get_data()
    print(data)
    

    
