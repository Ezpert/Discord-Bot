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
TOKEN = ''


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

        if user_message.lower() == "!cat":
            response = requests.get('https://cataas.com/cat')
            if response.status_code == 200:
                with open('cats.png', 'wb') as f:
                    f.write(response.content)
                await message.channel.send(file=discord.File('cats.png'))
                os.remove('cats.png')
            else:
                print("Failed to save the image")
        elif user_message == "!cat-hello":
            response = requests.get('https://cataas.com/cat/says/hello')
            if response.status_code == 200:
                with open('cats.png', 'wb') as f:
                    f.write(response.content)
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
