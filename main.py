"""
The MIT License (MIT)

Copyright (c) 2023-present ChameleonCord

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from dotenv import load_dotenv
from discord.ext import commands, tasks
import logging
import os
import discord


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.reactions = True
        super().__init__(command_prefix='$', intents=intents)

    async def setup_hook(self):
        self.background_task.start()
        # loading all cogs
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')

    async def close(self):
        await super().close()

    @tasks.loop(minutes=10)
    async def background_task(self):
        print('Running background task...')

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


if __name__ == '__main__':
    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    load_dotenv()
    token = os.getenv("DISCORD_BOT_TOKEN")
    from player_deck import DECK as playerDeckOne
    from category_deck import DECK as category_deck_one
    bot = Bot()
    bot.run(token=token, log_handler=handler, log_level=logging.DEBUG)
