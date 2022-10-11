import commands as cm
import imports
from dotenv import load_dotenv
load_dotenv()

token = imports.os.getenv("TOKEN")

intents = imports.discord.Intents.default()
intents.message_content = True

bot = imports.discord.Client(intents=intents)


commands = []
for fun in dir(cm):
    if not fun.startswith('__') and not fun.startswith('make'):
        commands.append(fun)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    # if message.channel.id != 747178040798347393:
    #     return
    # emote :P
    loser = imports.discord.utils.get(bot.emojis, name='pepeLoser')

    # message and args
    msg = message.content
    args = msg.split(' ')
    user_id = message.author.id

    # evaluate commands
    if msg == '.test':
        value = eval('cm.' + msg[1:] + '()')
        await message.reply(file=value[0], embed=value[1])
    elif len(args) > 1 and msg.startswith('.') and any(word in msg for word in commands):
        value = eval('cm.' + args[0][1:] + f'({args},{user_id})')
        await message.reply(embed=value)
    elif msg.startswith('.') and any(word in msg for word in commands):
        value = eval('cm.' + args[0][1:] + f'({user_id})')
        await message.reply(embed=value)
    else:
        await message.reply(f"Not a real command {loser} Try .help instead {loser}")


print(f'COMMANDS LIST: {commands}')

bot.run(token)
