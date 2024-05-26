import discord
from discord import app_commands
from discord.ext import commands
import openai
from functions.gpt import chatGPT
from functions.dado import Dado
from functions.gif import Gif
from functions.qrcode import QRCode
from keys.keys import masqueico_key, openai_key

# ============================================
# = Versao 2.1.0                           
# ============================================

openai.api_key = openai_key()

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        await client.tree.sync()
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('🐒')
        print('- - - - - - - -')

    async def on_message(client, message):
        if message.author.id == client.user.id:
            return

        if message.channel.name == 'masqueicogpt': #chatGPT
            await chatGPT.masqueicogpt(message)

        elif Dado.busca_dado(message): #dado
            busca = Dado.busca_dado(message)
            await Dado.roda_dado(busca=busca, message=message)

intents = discord.Intents.all()
client = MyClient(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)

@client.tree.command(description="sincroniza comandos com codigo (admin)")
async def sync(interaction: discord.Interaction):
    if (interaction.user.id != 353864784950591490):
        await interaction.response.send_message("comando para debug do codigo... apenas admins podem usar")
        return
    await client.tree.sync()
    await interaction.response.send_message("sync feito com sucesso!")

@client.tree.command(description="busca gif aleatorio")
async def gif(interaction: discord.Interaction, query: str):    
    await Gif.busca_gif(query, interaction)
    
@client.tree.command(description="gera qrcode a partir de uma entrada")
async def qrcode(interaction: discord.Interaction, texto: str):
    await QRCode(texto, interaction)
        
client.run(masqueico_key())