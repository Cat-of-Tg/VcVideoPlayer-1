from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from config import SOURCE_CODE, ASSISTANT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME
from plugins.tr import *
from pyrogram.errors import MessageNotModified

@Client.on_message(filters.command("start"))
async def start(client, message):
   buttons = [
            [
                InlineKeyboardButton("ADD ME TO UR GROUP", url=f"https://t.me/EIRA_LADBOT?startgroup=true"),
            ],
            [
                InlineKeyboardButton("UPSATES", url=f"https://t.me/Team_Lad"),
                InlineKeyboardButton("SUPPORT", url=f"https://t.me/teamladz_bothub"),
            ],
            [
                InlineKeyboardButton("DEV", url=f"https://t.me/cat_of_tg"),
            ],
            [
               InlineKeyboardButton("HELP & COMMANDS", callback_data="help"),
            ]
            ]
   reply_markup = InlineKeyboardMarkup(buttons)
   if message.chat.type == 'private':
       await message.reply_text(
          START_TEXT,
          reply_markup=reply_markup
       )
   else:
      await message.reply(f"**@{ASSISTANT_NAME} is Alive! ✨**")

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("BACK", callback_data="start"),
                InlineKeyboardButton ("SUPPORT", url=f"https://t.me/teamladz_bothub"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="about":
        buttons = [
            [
                InlineKeyboardButton("BACK", callback_data="start"),
                InlineKeyboardButton ("SUPPORT", url=f"https://t.me/teamladz_bothub"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                ABOUT_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="devs":
        buttons = [
            [
                InlineKeyboardButton("Lᴏᴜɪꜱ", url="https://t.me/DeeCodeBots"),
                InlineKeyboardButton("Eʀʀᴏʀ", url="https://t.me/ProErrorXD"),
            ],
            [
                InlineKeyboardButton("Bʟᴀᴢᴇ", url="https://t.me/piroXpower"),
                InlineKeyboardButton("Pʀɪɴᴄᴇ", url="https://t.me/DEVILDAD_PRINCE"),
            ],
            [
                InlineKeyboardButton("Hʏᴏᴋᴀ", url="https://t.me/Pratheek_XD"),
                InlineKeyboardButton("Zᴀʟɪᴍ", url="https://t.me/Jalim_Munda"),
            ],
            [
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                DEVS_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="start":
        buttons = [
            [
                InlineKeyboardButton("Hᴇʟᴘ & Cᴏᴍᴍᴀɴᴅꜱ", callback_data="help"),
            ],
            [
                InlineKeyboardButton('SUPPORT", url=f"https://teamladz_bothub"),
                InlineKeyboardButton("CHANNEL", url=f"https://t.me/team_lad"),
            ],
            [
                InlineKeyboardButton("ADD ME TO YOUR GROUP", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
            [
               InlineKeyboardButton("MY MASTER", url=f"https://t.me/CAT_OF_TG"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                START_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass
