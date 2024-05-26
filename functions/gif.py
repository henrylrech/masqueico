import json
import requests
import random
import discord
from datetime import datetime

class Gif():
    async def busca_gif(message: str, interaction: discord.Interaction):
        datetime.now()
        print(f'{datetime.now()} - gif -> query: {message} ({interaction.user})')

        try: 
            response = requests.get(f"https://tenor.googleapis.com/v2/search?q={str(message)}&key=AIzaSyBQcVVJiMmqJdnWeDaFxIa70O4tVZ-fA7I").text
            response_info = json.loads(response)
            final = random.choice(response_info['results'])['media_formats']['gif']['url']
            await interaction.response.send_message(final)
        except Exception as e:
            print(f"Exception: {e}")