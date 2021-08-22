import discord
from discord.ext import commands
from discord.utils import find


class Help(commands.Cog, name='Help'):
    def __init__(self, bot):
        self.bot = bot
        self.bot.remove_command('help')
        self.help_channels = [878903467488464906, 779445592560500819]

    @staticmethod
    def format_list(join_str, input_list):
        return join_str.join(f'`{element}`' for element in input_list)

    @commands.command(
        brief='List all commands',
        help='List all commands by category or get info on specific command usage',
        usage='[command]'
    )
    async def help(self, ctx, name=None):
        if ctx.channel.id not in self.help_channels:
            await ctx.send(f'Please use help commands in the help channel')
            return
        if name is not None:
            if command := find(lambda c: name == c.name or name in c.aliases, self.bot.commands):
                embed = discord.Embed(
                    title=f'{command.name} {command.usage or ""}',
                    description=command.help or command.brief,
                    color=discord.Color.teal()
                )

                if command.aliases:
                    embed.add_field(name='aliases', value=Help.format_list(', ', command.aliases))

                embed.set_footer(text=f'Category: {command.cog.qualified_name}')

            else:
                await ctx.send(f'Command `{name}` not found')
                return
        else:
            embed = discord.Embed(
                title='TBot commands',
                description=self.bot.description,
                color=discord.Color.purple()
            )

            for category, cog in self.bot.cogs.items():
                embed.add_field(
                    name=category,
                    value=Help.format_list(', ', cog.get_commands()) or '\u200B',
                    inline=False)

            embed.set_footer(text=f'For more, type {self.bot.command_prefix}help <command>')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
