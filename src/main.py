from discord.ext import commands
import discord
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)


#bot.author_id = 0000000  # Change to your discord id
bot.author_id = 0
@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

#Answer with username
@bot.command()
async def name(ctx):
    await ctx.send(ctx.message.author.name)

#Answer with random number between 1 and 6
@bot.command()
async def d6(ctx):
    await ctx.send(random.randint(1, 6))

#Elevate user to admin role
@bot.command(name='admin')
async def admin(ctx, user: discord.Member):
    #Check for role
    admin_role = discord.utils.get(ctx.guild.roles, name="Admin")
    if not admin_role:
        admin_role = await ctx.guild.create_role(name="Admin", permissions=discord.Permissions.all(), color=discord.Color.blue())    
    await user.add_roles(admin_role)

#Ban User with a reason message
@bot.command()
async def ban(ctx, user: discord.Member, *, reason=None):
    if not reason:
        reasons = ["By my hand be purged", "carreful with this ban hamm... fuck.", "ratio", "SOwOrry", "Lol u ded"]
        reason = random.choice(reasons)
    await user.ban(reason=reason)
    await ctx.send(f'Banned {user.mention}: {reason}')


#Add a bit of sarcasm... I need friends...
@bot.event
async def on_message(message):
    #So the JaajBot does not answer to himself 
    if bot.user.id != message.author.id:
        if message.content == 'Salut tout le monde':
            await message.reply(f'Salut tout seul {message.author.mention}')
    await bot.process_commands(message)


#token = "<MY_TOKEN>"
token = "" #Don't forget :)
bot.run(token)  # Starts the bot