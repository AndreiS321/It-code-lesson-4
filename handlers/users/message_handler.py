from aiogram import types
from utils import get_dog_img_url
from loader import dp, cli


@dp.message_handler()
async def send_dog(message: types.Message):
    img_url = await get_dog_img_url(cli)
    if not get_dog_img_url(cli):
        await message.answer("Не получилось подключиться к random.dog")
        return None
    await message.answer_photo(img_url)
