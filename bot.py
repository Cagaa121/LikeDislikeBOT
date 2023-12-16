import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from btn import *

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "6306000460:AAETRQkjNRl_mdOFmuXwKaaacfbil6NxY90"

bot = Bot(token=BOT_TOKEN, parse_mode="html")
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

async def set_my_bot_commands(dp: Dispatcher):
   await dp.bot.set_my_commands([
  types.BotCommand("start", "Start bot"),
  types.BotCommand("me", "Myself"),
])


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
  await message.answer("Salom")


@dp.callback_query_handler(text="like")
async def get_like_handler(call: types.CallbackQuery, state: FSMContext):
  data = await state.get_data()
  print(data)
  count = data['like']+1

  await state.update_data(like=count)
  btn = await get_text_inline_btn(like=count, dislike=data['dislike'])
  await call.message.edit_reply_markup(reply_markup=btn)
  await call.answer("Javob uchun raxmat", show_alert=True)


@dp.callback_query_handler(text="dislike")
async def get_like_handler(call: types.CallbackQuery, state: FSMContext):
  data = await state.get_data()
  count = data['dislike'] + 1

  await state.update_data(dislike=count)
  btn = await get_text_inline_btn(like = data['like'], dislike=count)
  await call.message.edit_reply_markup(reply_markup=btn)
  await call.answer("Javob uchun raxmat", show_alert=True)


@dp.message_handler(content_types=["text"])
async def get_text_handler(message: types.Message, state: FSMContext):
    text = message.text
    await state.update_data(like=0, dislike=0)
    btn = await get_text_inline_btn()
    await message.answer(text, reply_markup=btn)


if __name__ == "__main__":
 executor.start_polling(dp, on_startup=set_my_bot_commands)
