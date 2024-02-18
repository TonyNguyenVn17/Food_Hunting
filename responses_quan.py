from random import choice, randint
from typing import List

def get_response(user_input : str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1,6)}'
    elif 'event' in lowered:
        data = get_data()
        events = [event for event_list in data.values() for event in event_list]
        return events
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


def get_data() -> dict[str, List[dict[str, str]]]:
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
    

    
