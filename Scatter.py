import discord
from discord.ext import commands
import os

TOKEN = os.environ["DISCORD_TOKEN"]

# 指定目標使用者 ID（整數，不是名字）
TARGET_USER_ID = 932470377987334224

# 目標頻道 ID，要轉發到的頻道
TARGET_CHANNEL_ID = 1390240933093572700

# intents 要允許 message content
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"登入成功！機器人：{bot.user}")

@bot.event
async def on_message(message):
    # 忽略自己的訊息和其他機器人訊息
    if message.author.bot:
        return

    # 判斷是否是目標用戶
    if message.author.id == TARGET_USER_ID:
        target_channel = bot.get_channel(TARGET_CHANNEL_ID)
        if target_channel:
            files = []
            for attachment in message.attachments:
                file = await attachment.to_file()
                files.append(file)

            content = f"📢 {message.author.display_name} 在 {message.channel.mention} 說：\n{message.content}"

            await target_channel.send(content=content, files=files)

    # 保留指令功能
    await bot.process_commands(message)

bot.run(TOKEN)
