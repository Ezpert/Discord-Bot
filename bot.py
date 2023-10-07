import discord
import responses
from discord import Intents
from discord.ext import commands

# Enable all standard intents and message content
# (prefix commands generally require message content)
intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTE2MDMxNzY2NjgyNTg4MzY4OA.Gh7efN.rOGwqGHJk10sCYPcAbi0jr_z2drfqjimv4AecI'
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

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)

        elif user_message[0] == '!':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
