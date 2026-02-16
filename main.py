import asyncio
from bot.bot import DBot
import bot.config as config


bot = DBot()

async def main():
    async with bot:
        await bot.load_cogs()
        await bot.start(config.TOKEN)


if __name__ == '__main__':
    asyncio.run(main())
