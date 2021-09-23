import os
from datetime import datetime

from discord import Intents
from discord.ext import commands

from . import constants


class Bot(commands.Bot):
    """Something."""

    def __init__(self) -> None:
        intents = Intents.default()
        intents.members = True
        intents.presences = False

        super().__init__(command_prefix=constants.PREFIX, intents=intents)

        self.load_extensions()

        self.launch_time = datetime.utcnow().timestamp()

    def load_extensions(self) -> None:
        """Something."""
        for extension in constants.EXTENSIONS.glob("*/*.py"):
            if extension.name.startswith("_"):
                continue
            dot_path = str(extension).replace(os.sep, ".")[:-3]
            self.load_extension(dot_path)

    def run(self) -> None:
        """Something."""
        if constants.TOKEN is None:
            raise EnvironmentError(
                "Please make sure that you have your TOKEN initialized in .env"
            )

        super().run(constants.TOKEN)
