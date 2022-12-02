from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData(
    "buy", "item_name", "quantity"
)

inline_items_callback = CallbackData("buy", "name", "item_id")

like_callback = CallbackData("like", "reaction", "item_id")
