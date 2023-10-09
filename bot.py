import discord
import requests
import os

import responses
from discord import Intents
from discord.ext import commands
import requests

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = 'MTE2MDMxMjQ1MTM2ODIzOTE4NQ.GqglEN.En-k66fHwR6MCfiZfkGpMEuQo_G356j4nQshW0'


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"user_message: {user_message}")

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message.lower() == '!join':
            await join(message)
        elif user_message.lower() == '!disconnect':
            await disconnect(message)
        elif user_message.lower().startswith('!cat'):
            pic_times = 1
            try:
                command, pic_times, pic_text = user_message.split(' ', 2)
            except ValueError:
                print("Split unsuccessful. Unable to split the string.")
                try:
                    command, pic_text = user_message.split(' ', 1)
                except ValueError:
                    pic_text = ' '
                    print("Split unsuccessful. Unable to split the string.")

            for x in range(int(pic_times)):
                if not pic_text:
                    image = requests.get('https://cataas.com/cat')
                else:
                    image = requests.get('https://cataas.com/cat/says/' + pic_text)
                if image.status_code == 200:
                    with open('cats.png', 'wb') as f:
                        f.write(image.content)
                        await message.channel.send(file=discord.File('cats.png'))
                    os.remove('cats.png')
                else:
                    print("Failed to save the image")
        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        elif user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
