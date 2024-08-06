from string import punctuation

from aiogram import F, types, Router
from aiogram.types import Message

from filters.chat_types import ChatTypeFilter


user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))

restricted_words = {'кабан', 'заяц', 'лиса'}

def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()):
        await message.answer(f"{message.from_user.username}, соблюдайте порядок в чате!")
        await message.delete()
        # await message.chat.ban(message.from_user.id)
