import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from pyrogram import Client, filters
from bot import autocaption
from config import Config
from database.database import *
from translation import Translation
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_BUTTONS=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("📄 BOT STATUS", callback_data = "status_data")
              ], 
              [
                  InlineKeyboardButton("📫 UPDATES", url = "https://t.me/Ts_bots"), 
                  InlineKeyboardButton("📕 ABOUT", callback_data = "about_data")
              ], 
              [
                  InlineKeyboardButton("💡 HELP", callback_data = "help_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ] 
        ]
)

HELP_BUTTONS=InlineKeyboardMarkup(
        [
              [
                InlineKeyboardButton("ABOUT MARKDOWN", callback_data = "markdown_data")
              ], 
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
)

ABOUT_BUTTONS=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
) 


@Client.on_message(filters.command("start") & filters.private)
async def start(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.START_TEXT.format(update.from_user.first_name), 
          reply_to_message_id = cmd.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = START_BUTTONS
      )


@Client.on_message(filters.command("help") & filters.private)
async def help(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = update.message_id,
          parse_mode = "html",
          disable_web_page_preview = True,
          reply_markup = HELP_BUTTONS           
      )


@Client.on_message(filters.command("about") & filters.private)
async def about(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = update.message_id,
          parse_mode = "markdown",
          disable_web_page_preview = True, 
          reply_markup = ABOUT_BUTTONS
      )   
    
@Client.on_message(filters.command("set_caption") & filters.reply & filters.private)
async def set_caption(bot, update):
    if len(update.command) == 1:
        await update.reply_text(
            "**You can set your custom caption using this command!\nUse `/set_caption Your Caption` or Reply to your text with `/set_caption`**", 
            quote = True
        )
    else:
        command, caption = update.text.split(' ', 1)
        await update_caption(update.from_user.id, caption)
        await update.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
