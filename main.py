import discord
from discord.ext import commands

# Define intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot instance
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def join(ctx, channel_name: str):
    # Get the voice channel by name
    channel = discord.utils.get(ctx.guild.voice_channels, name=channel_name)
    if channel:
        await channel.connect()
        await ctx.send(f'Joined the voice channel: {channel_name}')
    else:
        await ctx.send(f'Channel "{channel_name}" not found.')

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send('Left the voice channel.')
    else:
        await ctx.send('I am not in a voice channel.')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
