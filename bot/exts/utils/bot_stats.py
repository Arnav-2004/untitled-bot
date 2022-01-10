from datetime import datetime
from platform import python_version

import humanize
from disnake import ApplicationCommandInteraction, Embed, __version__
from disnake.ext import commands

from bot.bot import Bot
from bot.constants import Colors


class BotStats(commands.Cog):
    """Get info about the bot."""

    def __init__(self, bot: Bot):
        self.bot = bot

    async def _make_ping_embed(self) -> Embed:
        return Embed(
            title="Pong!",
            description=f"Gateway Latency: {round(self.bot.latency * 1000)}ms",
            color=Colors.green,
        )

    async def _make_stats_embed(self) -> Embed:
        embed = Embed(
            title="Bot Stats",
            color=Colors.green,
        )

        embed.set_thumbnail(url=self.bot.user.display_avatar.url)

        uptime = humanize.precisedelta(
            datetime.utcnow().timestamp() - self.bot.launch_time
        )

        fields = {
            "Python Version": python_version(),
            "Disnake Version": __version__,
            "Uptime": uptime,
        }

        for name, value in list(fields.items()):
            embed.add_field(name=name, value=value, inline=False)

        return embed

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        """Ping the bot to see its latency."""
        await ctx.reply(embed=await self._make_ping_embed())

    @commands.slash_command(name="ping")
    async def slash_ping(self, inter: ApplicationCommandInteraction) -> None:
        """Ping the bot to see its latency."""
        await inter.send(embed=await self._make_ping_embed())

    @commands.command(name="stats")
    async def stats(self, ctx: commands.Context) -> None:
        """Get the information and current uptime of the bot."""
        await ctx.reply(embed=await self._make_stats_embed())

    @commands.slash_command(name="stats")
    async def slash_stats(self, inter: ApplicationCommandInteraction) -> None:
        """Get the information and current uptime of the bot."""
        await inter.send(embed=await self._make_stats_embed())


def setup(bot: Bot) -> None:
    """Loads the botstats cog."""
    bot.add_cog(BotStats(bot))
