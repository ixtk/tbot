from discord.ext import commands


class Dev(commands.Cog, name='Developer commands'):
    required_role = 'dev'

    def __init__(self, bot):
        self.bot = bot

    @commands.has_role(required_role)
    @commands.command(brief='Load extension.', help=f'Load extension. {required_role} role is required')
    async def load(self, ctx, extension):
        self.bot.load_extension(f'src.cogs.{extension}')
        await ctx.send(f'Extension `{extension}` loaded')

    @commands.has_role(required_role)
    @commands.command(brief='Unload extension.', help=f'Unload extension. {required_role} role is required')
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'src.cogs.{extension}')
        await ctx.send(f'Extension `{extension}` unloaded')

    @commands.has_role(required_role)
    @commands.command(brief='Reload extension.', help=f'Reload extension. {required_role} role is required')
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'src.cogs.{extension}')
        await ctx.send(f'Extension `{extension}` reloaded')


def setup(bot):
    bot.add_cog(Dev(bot))
