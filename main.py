from discord import embeds
import discord
from discord.ext import commands

f = open('.discordbottoken', 'r')

client = commands.Bot(command_prefix='')
token = f.readline()
f.close()

@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("저한테 DM으로 'Tomato'라고 말해보세요"))


@client.command(name='Tomato')
async def callmsg(message):
    await tomato(message)


@client.command(name='tomato')
async def callmsg(message):
    await tomato(message)

async def tomato(message):
    embed = discord.Embed(title="The TOMATO", description="당신은 감염되었습니다", color=0xf15f5f)
    embed.set_footer(text='당신의 상태 메시지를 "저한테 DM으로 "Tomato"라고 말해보세요"로 바꾸세요. 토마토 바이러스는 천천히 퍼질 것입니다. 단 하나의 규칙은 토마토를 말하는 이들을 위해서 게임을 스포일러해서는 안 됩니다.')

    await message.send(embed=embed)

client.run(token)