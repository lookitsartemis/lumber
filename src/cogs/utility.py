import nextcord
from nextcord.ext import commands
from nextcord import Interaction, Member, SlashOption
import platform

class Utilites(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xa67f71
        
    @commands.Cog.listener()
    async def on_ready(self):
        self.avatar = self.bot.user.avatar
        
    @nextcord.slash_command(description="Replies with bot information")
    async def bot(self, interaction: Interaction):
        ping = int(self.bot.latency * 1000)
        id = self.bot.user.id
        created_at = self.bot.user.created_at
        discord_timestamp = f"<t:{int(created_at.timestamp())}:F>"
        guilds = len(self.bot.guilds)
        users = sum(guild.member_count for guild in self.bot.guilds)
        python_version = platform.python_version()
        library_version = nextcord.__version__
        system = platform.system()
        release = platform.release()
        architecture = platform.architecture()[0]
        
        embed = nextcord.Embed(
            title="About Lumber",
            color=self.color,
            description="A leveling bot for Discord!"
        )
        embed.set_thumbnail(self.avatar.url)
        embed.add_field(name="ID", value=id)
        embed.add_field(name="Created At", value=discord_timestamp)
        embed.add_field(name="Latency", value=f"{ping}ms")
        embed.add_field(name="Guilds", value=f"{guilds}")
        embed.add_field(name="Users", value=f"{users}")
        embed.add_field(name="Creator", value="<@1241249326844350491>")
        embed.add_field(name="Python Version", value=python_version)
        embed.add_field(name="Nextcord Version", value=library_version)
        embed.add_field(name="Host System", value=f"{system} {release} ({architecture})")
        
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Utilites(bot))