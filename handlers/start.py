from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

LOVER_MUSIC_BOT_IMG= "https://telegra.ph/file/a76e3f40dcc50b7696993.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(LOVER_MUSIC_BOT_IMG)
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅
I am ππΌππ²πΏπ πππΆπ°ππΌπ, I Am an Advance And Powerful Telegram Groups Voice Chat Music Bot.For More Type /help to know my commands.
Note:- Add @LoverMusicBot and @LoverMusicAssistant to your group and make an admin.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  First Robot π ", url="https://t.me/LoverMusicRobot")
                  ],[
                    InlineKeyboardButton(
                        "CREATOR", url="https://t.me/SarcasticLucky"
                    ),
                    InlineKeyboardButton(
                        "π¬ Support Group", url="https://t.me/LoverMusicSupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π Assistant π", url="https://t.me/LoverMusicAssistant2"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "β Add To Your Group β", url="https://t.me/NewLoverMusicBot?startgroup=true"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "β LoverNetwork β", url="https://t.me/LoverNetwork"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**π Lover Music Bot is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ποΈ Support Group ποΈ", url="https://t.me/LoverMusicSupport")
                ]
            ]
        )
   )

