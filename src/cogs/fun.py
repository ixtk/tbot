from random import choice

from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='fact', brief='Get a random fact')
    async def get_fact(self, ctx):
        response = await self.bot.session.get(
            'https://uselessfacts.jsph.pl/random.json',
            params={'language': 'en'}
        )
        
        json_data = await response.json()
        emojis = [':eyes:', ':face_with_monocle:', ':thinking:']

        await ctx.send(f'{json_data["text"]} {choice(emojis)}')

    @commands.command(brief='Get a random number', help='Get a random number up to <n>')
    async def roll(self, ctx, n=100):
        await ctx.send(f'{ctx.message.author.name} rolled {choice(range(1, n + 1)):,}! :star2:')

    @commands.command(name='8ball', brief='Get a random answer', help='Get a random yes/no type of answer to your question')
    async def eight_ball(self, ctx, *, question):
        answers = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes',
            'Yes – definitely.',
            'You may rely on it.'
        ]

        await ctx.send(f'Question: {question}\nAnswer: {choice(answers)}')


def setup(bot):
    bot.add_cog(Fun(bot))
