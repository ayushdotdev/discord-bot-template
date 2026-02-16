import discord
from discord.ext import commands


class Bot(commands.Bot):
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


