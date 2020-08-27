import os
import random
import discord 
import time 

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix= '/')
client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

class CustomClient(discord.client):
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

client = CustomClient(discord.Client)

@client.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi {member.name}, welcome to World//Zero! Check out the #rules channel before you speak and, 
    you can view the pinned message in #announcements so see everyones real name!'
  )

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  noOneAsked = [
    'No one asked.',
    'Only clean vibes allowed!'
    (
        'But are you, really?'
    ),
    
  ]

  if message.content == 'im':
    response = random.choice(noOneAsked)
    await message.channel.send(response)
  if message.content == 'i love you':
    response = ("I love you too!")
@client.event
async def on_message(message):
  if message.content == 'fight':
    turn = random.randint(2)
    pstrength = random.randint(10, 15)
    cstrength = random.randint(10, 15)
    hp = 100
    chp = 100
    time.sleep(1)
    pstrength 


@client.event 
async def on_message(message):
  if message.content == 'rock':  
    Rnum = random.randint(1, 3)
    if Rnum == 1:
      print("Computer picked rock! It's a tie!")
    if Rnum == 2:
      print("Computer picked paper! Computer won!")
    if Rnum == 3:
      print("Computer picked scissors! You win!")
  
  if message.content == 'paper':
    Pnum = random.randint(1, 3)
    if Pnum == 1:
      print("Computer picked rock! You win!")
    if Pnum == 2:
      print("Computer picked paper! It's a tie!")
    if Pnum == 3:
      print("Computer picked scissors! Computer wins!")

  if message.content == '/scissors':
    Snum = random.randint(1, 3)
    if Snum == 1:
      print("Computer picked rock! Computer wins!")
    if Snum == 2:
      print("Computer picked paper! You win!")
    if Snum == 3:
      print("Computer picked scissors! It's a tie!")

    
client.run("NzQxMDEzOTk1OTM0NDQ5NjY0.XyxZEA._xbLjKHBLSyTBOiojzVgTyerCDM")