import discord
from discord.ext import commands
import bot.config as config

class DBot(commands.Bot):
    def __init__(self, **kwargs):
        intents = discord.Intents.default()
        intents.message_content = True
        allowed_mentions = discord.AllowedMentions(replied_user=False)

        super().__init__(
            intents=intents,
            command_prefix= commands.when_mentioned_or(config.PREFIX),
            allowed_mentions= allowed_mentions,
            **kwargs
        )

        async def load_cogs(self):
            import os

            cog_dir = ["bot/commands", "bot/listeners"]

            for dir in cog_dir:
                for cog in os.listdir(dir):
                    if cog.endswith(".py") and cog != "__init__.py":
                        path = cog[:-3]
                        extension = f"{dir.replace("/",".")}.{path}"

                        await self.load_extension(extension)



