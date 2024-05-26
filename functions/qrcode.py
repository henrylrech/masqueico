import qrcode
import discord
import os
from datetime import datetime

async def QRCode(entrada: str, interaction: discord.Interaction):
    img = qrcode.make(entrada)
    project_path = os.getcwd()
    path = fr'{project_path}\temp\qr.png'
    print(path)
    try:
        with open(path, 'wb') as qr:
            img.save(qr) 
    except FileNotFoundError:
        os.mkdir("./temp")
        with open(path, 'wb') as qr:
            img.save(qr) 

    picture = discord.File(path)
    print(f"{datetime.now()} - qrcode -> query: {entrada} ({interaction.user})")
    await interaction.response.send_message(file=picture)