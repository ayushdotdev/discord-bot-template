import discord
from discord.ext import commands
from discord import ButtonStyle
import bot.config as config

class general(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = 'help')
  async def help(self,ctx,*, cmd:str = None):
    prefix = config.PREFIX
    view = discord.ui.View()
    prev_btn =discord.ui.Button(
      label = "◀️",
      style = ButtonStyle.primary
      )
    next_btn = discord.ui.Button(
      label = "▶️",
      style = ButtonStyle.primary
      )
    view.add_item(prev_btn)
    view.add_item(next_btn)
    pages = []
    for cog_name,cog_object in self.bot.cogs.items():
      page = discord.Embed(
        title = f'*{cog_name} Commands*',
        color = 0xff00c8
        )
      for cmd in cog_object.get_commands():
        page.add_field(
          name = f'{prefix}{cmd.name}',
          value = cmd.help or "No description provided"
          )
      pages.append(page)
    current_page = 0
    async def prev_callback(interaction: discord.Interaction):
      nonlocal current_page
      current_page = max(current_page - 1,0)
      await interaction.response.edit_message(embed = pages[current_page],view = view)
    async def next_callback(interaction: discord.Interaction):
      nonlocal current_page
      current_page = max(current_page + 1,0)
      await interaction.response.edit_message(embed = pages[current_page],view = view)
    prev_btn.callback = prev_callback
    next_btn.callback = next_callback
    await ctx.send(embed = pages[current_page],view = view)
    
def setup(bot):
  bot.add_cog(general(bot))
