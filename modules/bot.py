import discord
from config import AppConfig
import log_utils
import os


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

        log_utils.log_bot(f"Logged on as {self.user}, Guild: {guild}, Target Channel: {target_channel}")

    async def on_message(self, message):
        if message.author != self.user:

            if message.content[0] == AppConfig.BOT_COMMAND_PREFIX:
                message_content = message.content.replace("!", "")

                content = "Not Found"

                if message_content == "list":
                    content = " ".join(os.listdir(AppConfig.LOG_FILES_DIR_PATH))

                elif message_content.split(" ")[0] == "get" and len(message_content.split(" ")) == 2:

                    file = message_content.split(" ")[1]
                    log_files = os.listdir(AppConfig.LOG_FILES_DIR_PATH)

                    if file in log_files:
                        content = log_utils.read_log_file(file)

                elif message_content == "help":
                    content = "list, get"

                await message.channel.send(content)
