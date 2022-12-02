import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_dates import inline_items_callback, like_callback

inline_buttons = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(
                                                  text="Купить товар",
                                                  callback_data="1"
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text=emoji.emojize(":thumbs_up:"),
                                                  callback_data="1"
                                              ),
                                              InlineKeyboardButton(
                                                  text=emoji.emojize(":thumbs_down:"),
                                                  callback_data="1"
                                              )
                                          ],
                                          [
                                              InlineKeyboardButton(
                                                  text="Поделиться с другом",
                                                  callback_data="1"
                                              )
                                          ]
                                      ]
                                      )


def create_button(id: int):
    return InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                            text="Купить товар",
                                            callback_data=inline_items_callback.new(
                                                name="Купить",
                                                item_id=id
                                            )
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text=emoji.emojize(":thumbs_up:"),
                                            callback_data=like_callback.new(
                                                reaction="like",
                                                item_id=id
                                            )
                                        ),
                                        InlineKeyboardButton(
                                            text=emoji.emojize(":thumbs_down:"),
                                            callback_data=like_callback.new(
                                                reaction="dislike",
                                                item_id=id
                                            )
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text="Поделиться с другом",
                                            callback_data=like_callback.new(
                                                reaction="share",
                                                item_id=id
                                            )
                                        )
                                    ]
                                ]
                                )
