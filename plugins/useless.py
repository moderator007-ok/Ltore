from bot import Bot
from pyrogram.types import Message
from pyrogram import filters
from config import ADMINS
from datetime import datetime
from helper_func import get_readable_time

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))

BOT_STATS_TEXT = "<b>BOT UPTIME: {uptime}</b>"    

"""
@Bot.on_message(filters.private & filters.incoming)
async def useless(_, message: Message):
    if message.from_user.id in ADMINS:
        print(f"Admin {message.from_user.id} tried to access the useless function.")
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)


BOT_STATS_TEXT = "<b>BOT UPTIME: {uptime}</b>"
USER_REPLY_TEXT = "<blockquote><b>Don't send me messages directly I'm only File Share bot!\n Contact Bot Developer: @StupidBoi69</b></blockquote>"
"""
