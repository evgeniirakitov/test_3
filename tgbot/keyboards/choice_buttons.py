from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_dates import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text="КУпи грушу",
                                          callback_data=buy_callback.new(
                                              item_name="pear",
                                              quantity=1
                                          )
                                      ),
                                      InlineKeyboardButton(
                                          text="Купи яблоки",
                                          callback_data="buy:apple:5"
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text="Отмена",
                                          callback_data="cancel"
                                      )
                                  ]
                              ]
                              )

pear_keyboard = InlineKeyboardMarkup()

PEAR_LINK = "https://google.com"

pear_link = InlineKeyboardButton(text="Купи тут", url=PEAR_LINK)

pear_keyboard.insert(pear_link)
