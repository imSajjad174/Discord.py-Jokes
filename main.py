import discord
from discord_slash import SlashCommand, SlashContext
import requests

intents = discord.Intents.default()
intents.messages = True

bot = discord.Client(intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@slash.slash(name="joke", description="Get a random joke")
async def joke(ctx: SlashContext):
    joke = get_joke()
    await ctx.send(joke)

def get_joke():
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    joke_data = response.json()

    if joke_data['type'] == 'single':
        joke = joke_data['joke']
    else:
        joke = f"{joke_data['setup']}\n{joke_data['delivery']}"

    return joke

TOKEN = 'your_discord_bot_token'
bot.run(TOKEN)
