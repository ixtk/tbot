import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.role_message_ids = [856250741694136341, 856447452533751818]
        self.emoji_to_role = {
            '🟢': 856251410353618955,
            '🟡': 856251467715313704,
            '🎉': 856447097892110357
        }

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id not in self.role_message_ids:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        role_id = self.emoji_to_role.get(payload.emoji.name)
        if role_id is None:
            return

        role = guild.get_role(role_id)
        if role is None:
            return
        
        await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id not in self.role_message_ids:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if guild is None:
            return

        role_id = self.emoji_to_role.get(payload.emoji.name)
        if role_id is None:
            return

        role = guild.get_role(role_id)
        if role is None:
            return
        
        member = guild.get_member(payload.user_id)
        if member is None:
            return
        
        await member.remove_roles(role)

    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    @commands.command(brief='Ban the user', usage='<user>')
    async def ban(self, ctx, member: discord.User, *, reason=None):
        if reason is None:
            reason = 'being a jerk'
        
        await member.send(f'You have been banned from {ctx.guild.name} for {reason}')
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f'{member.name} has been banned from the server.')

    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    @commands.command(brief='Unban the user', usage='<username#discriminator>')
    async def unban(self, ctx, member):
        banned_users = await ctx.guild.bans()
        name, discriminator = member.split('#')

        for banned in banned_users:
            if banned.user.name == name and banned.user.discriminator == discriminator:
                await ctx.guild.unban(banned.user)

                await ctx.send(f'{member} has been unbanned from the server.')

    @commands.has_guild_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    @commands.command(brief='Kick the user', usage='<user>')
    async def kick(self, ctx, member: discord.User, *, reason=None):
        if reason is None:
            reason = 'being a jerk'

        await member.send(f'You have been kicked from {ctx.guild.name} for {reason}')
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f'{member.name} has been kicked from the server.')


def setup(bot):
    bot.add_cog(Moderation(bot))
