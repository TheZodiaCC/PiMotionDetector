import discord
from config import AppConfig


class RPiMotionDetectorBOT(discord.Client):
    def __init__(self):
        super().__init__()

    def get_guild(self):
        return discord.utils.get(self.guilds, name=AppConfig.DISCORD_TARGET_GUILD)

    def get_target_channel(self):
        guild = self.get_guild()

        return discord.utils.get(guild.channels, name=AppConfig.DISCORD_TARGET_CHANNEL)

    async def on_ready(self):
        guild = self.get_guild()
        target_channel = self.get_target_channel()

        print(f"Logged on as {self.user}, Guild: {guild}, Target Channel: {target_channel}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
