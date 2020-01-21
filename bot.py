
import asyncio, aiohttp, discord, os, re
import wikipedia
import random


#wikipedia code analyzer/webscraper
def wiki_summary(arg):
    definition = wikipedia.summary(arg, sentences=1, chars=100, 
    auto_suggest=True, redirect=True)

    return definition

#rps code that determines the winner
def rps(arg, arg2):
        if arg == 'rock':

            if arg2=='paper':
                msg='I won so, you are bad'

            elif arg2=="rock":
                msg="We tied, go again if you are a man"

            else:
                msg="Darn it, you win..."

        elif arg == "scissors":

            if arg2=="paper":
                msg="Darn it, you win..."

            elif arg2=="rock":
                msg="I won so, you are bad"

            else:
                msg="We tied, go again if you are a man"

        elif arg == "paper":

            if arg2=="paper":
                msg="We tied, go again if you are a man"

            elif arg2=="rock":
                msg="Darn it, you win..."

            else:
                msg="I won so, you are bad"

        else:
            msg="You can't even play rock paper scissors? Kinda sad."

        return ("I got "+ arg2 + ". " +msg)


#main class and body of the code
class custombotbydop(discord.Client):
    #connect the code with the bot
    async def on_ready(self):
        print('Logged in as {0.user.name} (ID: {0.user.id} ) | {1} servers'.format(self, str(len(self.servers))))
        await self.change_presence(game=discord.Game(name='with my gek and dop'))

    #commands and fucntions
    #includes custom commands and artificial intelligence
    async def on_message(self, message):
        words = message.content.split()

        if not message.author.bot and (not message.server or message.server.me in message.mentions):
            await self.send_typing(message.channel)

            try:
                input = re.sub('<@!?'+self.user.id+'>', '', message.content).strip()
                params = {'botid': 'b0dafd24ee35a477', 'custid': message.author.id, 'input': input or 'Hello'}
                async with http.get('https://www.pandorabots.com/pandora/talk-xml', params=params) as resp:

                    if resp.status == 200:
                        text = await resp.text()
                        text = text[text.find('<that>')+6:text.rfind('</that>')]
                        text = text.replace('&quot;','"').replace('&lt;','<').replace('&gt;','>').replace('&amp;','&').replace('<br>',' ')
                        await self.send_message(message.channel, text)

                    else:
                        await self.send_message(message.channel, 'Darn it I broke for a second')

            except asyncio.TimeoutError:
                await self.send_message(message.channel, 'My head just broke to be honest')

        #basic hello command
        if words[0].lower() =='-hello':
            msg = 'Hello {0.author.mention} what is up pal?'.format(message)
            await self.send_message(message.channel, msg)

        #wikipedia search command
        if words[0].lower() == "-define":
            important_words = words[1:]
            await self.send_message(message.channel, wiki_summary(important_words))
        
        #Lists out all possible commands
        if words[0].lower() == "-help":
            msg = "```Here is a list of commands that can be useful:\n\n\n-help will grant a list of commands\n\n-hello will greet the user\n\n-define [content] will define any term besides umbrella terms\n\n-flipcoin will flip a coin and print heads or tails\n\n-dice will produce a random value between 1 and 6 inclusive\n\n-about will tell you about the creation of this bot\n\n-rps [rock,paper,scissors] will play a game of rock paper scissors\n\n\nFinally, if you want to have a nice conversation with the robot, you can simply mention him (@gok).```".format(message)
            await self.send_message(message.channel, msg)

        #flips a coin and displays heads or tails
        if words[0].lower() == "-flipcoin":
            value=random.randint(0,1)
            msg=""
            if value ==1:
                msg="heads"
                print(value)
            else:
                msg="tails"
                print(value)
            await self.send_message(message.channel, msg)
        
        #rolls a 6 sided dice and displays the number
        if words[0].lower() =="-dice":
            value=random.randint(1,6)
            msg=value
            await self.send_message(message.channel, msg)

        #about gives a run down on the creation of the bot
        if words[0].lower() =="-about":
            msg="The creators, Hae Chan (dop) and Keagan (gek) both worked on this program extensively over the last two weeks in order to create a basic yet versatile discord robot with numerous unique features, including a working chatbot. Hae Chan programmed the bulk of the commands along with the web scraping capabilites and gek primarily coded the artificial intelligent robot that takes online data and transfers it to discord.".format(message)
            await self.send_message(message.channel, msg)

        #rock paper scissors basic game
        if words[0].lower() == "-rps":
            important_words = words[1:]
            important_word=words[1]
            print(important_words)
            print(important_word)
            value=random.randint(0,2)
            msg=""
            rps_value=""
            if value ==0:
                rps_value="rock"
                print(value)
                print(rps_value)
            elif value ==1:
                rps_value="scissors"
                print(value)
                print(rps_value)
            else:
                rps_value="paper"
                print(value)
                print(rps_value)
            

            await self.send_message(message.channel, rps(important_word, rps_value))

        

#boot up code
print('Starting...')
http = aiohttp.ClientSession()

#connects specific bot with code
custombotbydop().run('TOKEN')








