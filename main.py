from typing import Final
import os 
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses_quan import get_response

# Load the TOKEN (from safe place)
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Steup BOT
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probaly')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    
    try:
        response: str = get_response(user_message)
        # If it is a private message --> send back to the author 
        # Otherwise, answering directly to the Channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Handling the startup for our bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling incoming message
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

# MAIN entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()