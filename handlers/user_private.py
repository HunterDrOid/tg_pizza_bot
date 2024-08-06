from aiogram import F, types, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: Message) -> None:
    await message.answer('Привет, я виртуальный помощник!')


# @user_private_router.message(F.text.lower() == "меню")
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == "меню")))
async def menu_cmd(message: Message):
    await message.answer('Вот меню:')
    
@user_private_router.message(or_f(Command('about'), (F.text.lower() == "о нас:")))
# @user_private_router.message(Command('about'))
async def about_cmd(message: Message):
    await message.answer('о нас:')
    

@user_private_router.message(or_f(Command('payment'), (F.text.lower() == "варианты оплаты:")))
# @user_private_router.message(Command('payment'))
async def payment_cmd(message: Message):
    await message.answer('Варианты оплаты:')
    
    
@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки'))   
@user_private_router.message(Command('shipping'))
async def menu_cmd(message: Message):
    await message.answer('Варианты доставки:')
    

