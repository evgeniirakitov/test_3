import logging

from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.callback_dates import inline_items_callback, like_callback
from tgbot.keyboards.inline_buttons_1 import create_button

items = {1: 'https://www.gastronom.ru/binfiles/images/20191113/bd570867.jpg',
         2: 'https://www.gastronom.ru/binfiles/images/20191113/bd570867.jpg'}


async def user_start(message: Message):
    await message.reply(f"Hello, user! {message.from_user.id}")


async def show_items(message: Message):
    await message.answer_photo(
        photo=items.get(1),
        reply_markup=create_button(1)
    )
    await message.answer_photo(
        photo=items.get(2),
        reply_markup=create_button(2)
    )


async def buying_items(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"callback_data = {call.data}")
    item_id = int(callback_data.get("item_id"))

    await call.message.edit_caption(caption=f"Покупай товар номер {item_id}")


async def like(call: CallbackQuery, callback_data: dict):
    logging.info(f"callback_data = {call.data}")
    item_id = int(callback_data.get("item_id"))

    await call.answer("Тебе понравился этот товар", show_alert=False)


async def dislike(call: CallbackQuery, callback_data: dict):
    logging.info(f"callback_data = {call.data}")
    item_id = int(callback_data.get("item_id"))

    await call.answer(text="Тебе не понравился этот товар", show_alert=False)


async def share(call: CallbackQuery, callback_data: dict):
    logging.info(f"callback_data = {call.data}")
    item_id = int(callback_data.get("item_id"))

    await call.answer(text="Тебе не понравился этот товар", show_alert=False)
    await call.bot.edit_message_text(text="text")

def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(show_items, commands=["items"], state="*")
    dp.register_callback_query_handler(buying_items, inline_items_callback.filter(name="Купить"))
    dp.register_callback_query_handler(like, like_callback.filter(reaction="like"))
    dp.register_callback_query_handler(dislike, like_callback.filter(reaction="dislike"))
    dp.register_callback_query_handler(share, like_callback.filter(reaction="share"))
