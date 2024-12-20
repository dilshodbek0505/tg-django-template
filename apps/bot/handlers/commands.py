from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __


router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message, state: FSMContext):
    await message.answer(_("Botga xush kelibsiz!"))
