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
        if message.author != self.user and self.get_target_channel().name == AppConfig.DISCORD_TARGET_CHANNEL:
            if message.content[0] == AppConfig.BOT_COMMAND_PREFIX:

                await message.channel.send(self.commands_handler(message))

    def commands_handler(self, command):
        command_content = command.content.replace("!", "")

        output = "Not Found"

        if command_content == "list":
            output = self.list_command()

        elif command_content.split(" ")[0] == "get" and len(command_content.split(" ")) == 2:
            output = self.get_command(command_content)

        elif command_content == "help":
            output = "list\nget\n"

        return output

    def list_command(self):
        return " ".join(os.listdir(AppConfig.LOG_FILES_DIR_PATH))

    def get_command(self, command):
        output = ""

        file = command.split(" ")[1]
        log_files = os.listdir(AppConfig.LOG_FILES_DIR_PATH)

        if file in log_files:
            raw_output = log_utils.read_log_file(file)
            raw_output= "_".join(raw_output).replace("\n", "").split("_")[-50:]

            output = "\n".join(raw_output)

        return output
