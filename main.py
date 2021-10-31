import aiogram
import datetime
import random
import time
import requests
import io
from textwrap import wrap
from gtts import gTTS
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.helper import Helper, HelperMode, ListItem
from html import escape
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from aiogram.utils.exceptions import BotBlocked
import asyncio
from aiogram.utils.exceptions import Unauthorized
from aiogram.dispatcher import DEFAULT_RATE_LIMIT
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from io import StringIO
import sys
from aiogram.utils.exceptions import Throttled
import socket
from aiogram.types import ContentType
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from config import TOKEN
import os
import re
import json
import base64
import asyncio
from typing import List




import config




bot = aiogram.Bot(config.TOKEN, parse_mode='HTML')
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['help', 'cmd', 'хелп'], commands_prefix='!./')
async def profcheck(message):
    await message.reply(f"привет дай мне админку для начала а дальше \n Помощь по командам: \n /ban причина - банит \n /unban причина - разбанит \n /mute причина - мутит \n /unmute причина - размутит\n /help - дает помошь ")



@dp.message_handler(commands=['бан', 'ban'], commands_prefix='!./', is_chat_admin=True)
async def cmd_ban(message):
  comment = " ".join(message.text.split()[1:])
  admin_mention = message.from_user.mention
  banned_user_mention = message.reply_to_message.from_user.mention
  await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
  await message.reply(f"глава котов: {admin_mention}\nстер: {banned_user_mention}\nСрок: навсегда\nПричина: {comment}")

@dp.message_handler(commands=['разбан', 'unban'], commands_prefix='!./', is_chat_admin=True)
async def cmd_unban(message):
  await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
  admin_mention = message.from_user.mention
  banned_user_mention = message.reply_to_message.from_user.mention
  await message.reply(f"глава котов: {admin_mention}\nпомиловал: {banned_user_mention}")

@dp.message_handler(commands=['размут', 'unmute'], commands_prefix='!./', is_chat_admin=True)
async def cmd_unmute(message):
  await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
  admin_mention = message.from_user.mention
  muted_user_mention = message.reply_to_message.from_user.mention
  await message.reply(f"глава котов: {admin_mention}\nпомиловал: {muted_user_mention}")

@dp.message_handler(commands=['мут', 'м', 'mute'], commands_prefix='!./', is_chat_admin=True)
async def cmd_mute(message):
    comment = " ".join(message.text.split()[1:])
#   mutime = int(" ".join(message.text.split()[1]))
    admin_mention = message.from_user.mention
    muted_user_mention = message.reply_to_message.from_user.mention
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=datetime.timedelta(hours=1))
    await message.reply(f"глава котов: {admin_mention}\nЗамутил: {muted_user_mention}\nСрок: 1ч\nПричина: {comment}")
    
@dp.message_handler(commands=['start', 'старт'], commands_prefix='!./')
async def on_user_joined(message: types.Message):
      await message.reply('ку я работаю  ')
      await message.delete()


    


@dp.message_handler(commands=['пиу'], commands_prefix='!./')
async def profcheck(message):
    await message.reply(f" пау ")


a = int(100)
b = input("какое вы хотите слово поставить: ")

@dp.message_handler(commands="reid")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["рейд", "r"]
    keyboard.add(*buttons)
    await message.answer("привет это рейд", reply_markup=keyboard)
# from aiogram.dispatcher.filters import Text
@dp.message_handler(Text(equals="рейд"))
async def with_puree(message: types.Message):
    for _ in range(a):
        await message.reply(b)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
