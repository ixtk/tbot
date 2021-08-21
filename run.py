import logging
import os

import discord

from src.tbot import Tbot


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    intents = discord.Intents.default()
    intents.members = True

    bot = Tbot(command_prefix='>', intents=intents, description='Developed by ettx#3316')

    bot.run(os.getenv('BOT_TOKEN'))
