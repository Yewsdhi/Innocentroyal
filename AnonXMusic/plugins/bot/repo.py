from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AnonXMusic import app
from config import BOT_USERNAME

start_txt = """
❖ ʜᴇʏ , ᴛʜᴇʀᴇ ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ  ♥︎\n\n● ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ɴ ʏ ᴋ ᴀ ᴀ ♡゙, ʙᴏᴛ ʀᴇᴘᴏ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴄᴏʟʟᴇᴄᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ 🇹​​​​​​​​​​​​​​​​​​​​🇺​​​​​​​​​​​​​​​​​​​​🇱​​​​​​​​​​​​​​​​​​​​🇮​​​​​​​​​​​​​​​​​​​​🇵​​​​​​​​​​​​​​​​​​​​ ✘ 🇲​​​​​​​​​​​​​​​​​​​​🇺​​​​​​​​​​​​​​​​​​​​🇸​​​​​​​​​​​​​​​​​​​​🇮​​​​​​​​​​​​​​​​​​​​🇨​​​​​​​​​​​​​​​​​​​​"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/NatkhatAssociation"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://github.com/Unique980/MUSIC")
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/48d3867531bec52dac64f.png",
        caption=start_txt,
        reply_markup=reply_markup
    )
  
