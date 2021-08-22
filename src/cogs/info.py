from datetime import datetime

import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    def add_fields(embed, data):
        embed.add_field(
            name='Confirmed',
            value=f'{data.get("TotalConfirmed"):,} ({data.get("NewConfirmed"):,} recent)', inline=False)

        embed.add_field(
            name='Deaths',
            value=f'{data.get("TotalDeaths"):,} ({data.get("NewDeaths"):,} recent)', inline=False)

        embed.add_field(
            name='Recovered',
            value=f'{data.get("TotalRecovered"):,} ({data.get("NewRecovered"):,} recent)', inline=False)

    @commands.command(brief='Show covid-19 data', usage='[alpha_code]', aliases=['c19'])
    async def covid(self, ctx, country_code=None):  
        response = await self.bot.session.get('https://api.covid19api.com/summary')

        data = await response.json(content_type=None)
        if country_code:
            country_data = data.get('Countries')
            country = list(filter(lambda country: country.get('CountryCode') == country_code.upper(), country_data))[0]
            embed = discord.Embed(
                color=discord.Color.green(),
                title=f'Covid-19 stats for {country.get("Country")} :flag_{country_code}:')

            self.add_fields(embed, country)
        else:
            global_data = data.get('Global')

            embed = discord.Embed(
                color=discord.Color.green(),
                title='Global Covid-19 stats :mask:'
            )

            self.add_fields(embed, global_data)

        last_updated = datetime.strptime(data['Date'], '%Y-%m-%dT%H:%M:%S.%fZ')
        embed.set_footer(text=f'Last updated: {last_updated:%b %d, %Y %H:%M}')

        await ctx.send(embed=embed)

    @commands.command(
        name='serverinfo',
        help='Display some server stats',
        aliases=['sinfo']
    )
    async def server_info(self, ctx):
        guild = ctx.guild
        roles = ' '.join((str(role.mention) for role in guild.roles[1:]))

        embed = discord.Embed(
            title=f'Server information for {guild.name}',
            color=discord.Color.red())

        embed.add_field(name=':scroll: General', value=f'''
            **Owner**: {guild.owner}
            **Region**: {guild.region},
            **Created at**: {guild.created_at.strftime("%d %b, %Y")}
            **Verification level**: {guild.verification_level}''', inline=False)

        embed.add_field(name=':bar_chart: Stats', value=f'''
            **Member count**: {guild.member_count}
            **Bots**: {len(list(filter(lambda member: member.bot, guild.members)))}
            **Emoji count**: {len(guild.emojis)}
            **Text channels**: {len(guild.text_channels)}
            **Voice channels**: {len(guild.voice_channels)}
            **Roles**: {roles}''')

        embed.set_thumbnail(url=guild.icon_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
