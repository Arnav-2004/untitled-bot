from datetime import datetime
from platform import python_version

import humanize
from disnake import Embed, __version__
from disnake.ext import commands

from bot.bot import Bot
from bot.constants import Colors


class BotStats(commands.Cog):
    """Get info about the bot."""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        """Ping the bot to see its latency."""
        embed = Embed(
            title="Pong!",
            description=f"Gateway Latency: {round(self.bot.latency * 1000)}ms",
            color=Colors.green,
        )
        await ctx.reply(embed=embed)

    @commands.command()
    async def stats(self, ctx: commands.Context) -> None:
        """Get the information and current uptime of the bot."""
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
        await ctx.reply(embed=embed)


def setup(bot: Bot) -> None:
    """Loads the botstats cog."""
    bot.add_cog(BotStats(bot))
