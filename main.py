import discord
from discord.ext import commands
from discord_slash import SlashCommand
from token import TOKEN

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
  await ctx.send("check")


bot.run(TOKEN)
