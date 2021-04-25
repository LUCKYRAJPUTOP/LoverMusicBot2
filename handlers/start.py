from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

LOVER_MUSIC_BOT_IMG= "https://telegra.ph/file/a76e3f40dcc50b7696993.jpg"

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_photo(LOVER_MUSIC_BOT_IMG)
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵
I am Group Music Probot, I Am an Advance And Powerful Telegram Groups Voice Chat Music Bot.
Note:- Add @LoverMusicRobot2 and @LoverOwner2 to your group and make an admin.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 First Robot 🛠", url="https://t.me/LoverMusicRobot")
                  ],[
                    InlineKeyboardButton(
                        "CREATOR", url="https://t.me/SarcasticLucky"
                    ),
                    InlineKeyboardButton(
                        "💬 Support Group", url="https://t.me/LoverMusicSupport"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "💁 Assistant 💁", url="https://t.me/LoverOwner2"
                    )],
                    [ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/LoverMusicBotBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**💜 Group Music Probot is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Support Group 🎙️", url="https://t.me/LoverMusicSupport")
                ]
            ]
        )
   )

