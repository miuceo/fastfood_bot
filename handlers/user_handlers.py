from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from .buttons import register_kb, registered_kb

from database import get_users

user_router = Router()

@user_router.message(CommandStart())
@user_router.message(F.text == "🔙 Ortga")
@user_router.message(F.text == "User panelga qaytish")
async def cmd_start(message:Message, state:FSMContext):
    
    user = message.from_user
    data = get_users(user.id)
    if not data:
        await message.answer(
            text = '''🍔 FastFood Botga xush kelibsiz! 🚀

Buyurtma berishdan oldin ro‘yxatdan o‘tishingiz kerak.
Iltimos, quyidagi ma’lumotlarni yuboring:

👤 Ismingiz
📱 Telefon raqamingiz (+998 formatda)
📍 Yetkazib berish manzilingiz

ℹ️ Ma’lumotlaringiz faqat buyurtmalar uchun ishlatiladi.
            ''',
            reply_markup=register_kb
        )
    else:
        await message.answer(
            text = "Siz avval ro'yxatdan o'tgansiz, iltimos kerakli tugmani tanlang: ",
            reply_markup=registered_kb
        )
        
    