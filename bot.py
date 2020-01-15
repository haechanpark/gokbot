import discord

TOKEN = 'NjY3MDc3MzAxODc1Mzc2MTQ5.Xh9eNg.S9hNo6HXJlnXYc3qe4IndYfn4tk'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)









