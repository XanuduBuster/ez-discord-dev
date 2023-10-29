import discord
from discord.ext import commands
from discord_slash import SlashCommand
from token import TOKEN
from keep_alive import keep_alive

keep_alive()
token = os.environ.get(TOKEN)
client.run(TOKEN)

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@slash.slash(name="test", description="test bot command.")
async def test(ctx):
    await ctx.send("wokring")

@slash.slash(name="get_badge", description="get Developer Badge")
async def new_command(ctx):
    await ctx.send("you must run the test and this command multiple times, after this wait for 24 - 48 hours and check if you can claim the dev badge, if this didnt work, DM `xanudubuster`. thanks.")

bot.run(TOKEN)
