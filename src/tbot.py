from pathlib import Path

from discord.ext import commands
import aiohttp


class Tbot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for cog in Path('src/cogs').iterdir():
            if not cog.stem.startswith('_'):
                self.load_extension(f'src.cogs.{cog.stem}')
                print(f'{cog.name} loaded')

        self.session = aiohttp.ClientSession()

    async def on_command_error(self, ctx, exception):
        await ctx.send('Something went wrong')
        return await super().on_command_error(ctx, exception)

    async def close(self): 
        await self.session.close()
        await super().close()

    @staticmethod
    async def on_ready():
        print('Connected')
