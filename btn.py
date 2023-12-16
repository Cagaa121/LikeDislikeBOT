from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_text_inline_btn(like=0, dislike=0):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton(text=f"👍 {like}", callback_data="like"),
        InlineKeyboardButton(text=f"👎 {dislike}", callback_data="dislike")
    )

    return btn