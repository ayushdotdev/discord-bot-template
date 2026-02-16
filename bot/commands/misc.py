from discord.ext import commands

class misc(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = "ping", help = "Check latency of the bot")
  async def ping(self,ctx):
    latent = round(self.bot.latency * 1000)
    await ctx.send(f"Pong! Latency {latent} ms")


async def setup(bot):
  await bot.add_cog(misc(bot))
