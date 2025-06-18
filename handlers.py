from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from texts import TEXTS
from keyboards import get_main_menu, get_directions_menu, get_lang_menu, get_back_menu, get_apply_direction_menu
from utils import set_user_lang, get_user_lang
from config import MANAGER_CONTACT

user_state = {}

def register_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start(client, message: Message):
        user_state[message.from_user.id] = {}
        await message.reply("👋 Привет! Выберите язык:", reply_markup=get_lang_menu())

    @app.on_callback_query()
    async def callbacks(client, callback_query: CallbackQuery):
        user_id = callback_query.from_user.id
        data = callback_query.data

        if data.startswith("lang_"):
            lang = data.split("_")[1]
            set_user_lang(user_id, lang)
            await callback_query.message.edit_text(TEXTS[lang]["main"], reply_markup=get_main_menu(lang))

        elif data == "directions":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["directions"], reply_markup=get_directions_menu(lang))


        elif data.startswith("dir_"):

            lang = get_user_lang(user_id)

            dir_key = data.split("_")[1]

            await callback_query.message.edit_text(

                TEXTS[lang]["dir_info"].format(

                    dir_name=TEXTS[lang]["dir_names"][dir_key],

                    dir_desc=TEXTS[lang]["dir_descs"][dir_key]

                ),

                reply_markup=get_back_menu(lang)

            )

        elif data == "admission":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["admission"], reply_markup=get_back_menu(lang))

        elif data == "contact":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["contact"], reply_markup=get_back_menu(lang))

        elif data == "location":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["location"], reply_markup=get_back_menu(lang))

        elif data == "faq":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["faq"], reply_markup=get_back_menu(lang))

        elif data == "video":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["video"], reply_markup=get_back_menu(lang))

        elif data == "apply":
            user_state[user_id] = {"step": "name"}
            await callback_query.message.edit_text("📝 Введите ваше имя:")

        elif data == "back":
            lang = get_user_lang(user_id)
            await callback_query.message.edit_text(TEXTS[lang]["main"], reply_markup=get_main_menu(lang))

    @app.on_message(filters.text)
    async def handle_text(client, message: Message):
        user_id = message.from_user.id
        if user_id not in user_state or "step" not in user_state[user_id]:
            return

        step = user_state[user_id]["step"]

        if step == "name":
            user_state[user_id]["name"] = message.text
            user_state[user_id]["step"] = "phone"
            await message.reply("📱 Введите ваш номер телефона:")
        elif step == "phone":
            user_state[user_id]["phone"] = message.text
            user_state[user_id]["step"] = "direction"
            await message.reply("📚 Выберите направление:", reply_markup=get_apply_direction_menu())
        elif step == "comment":
            user_state[user_id]["comment"] = message.text
            data = user_state[user_id]
            text = f"""📥 Новая заявка:
            👤 Имя: {data['name']}
            📱 Телефон: {data['phone']}
            📚 Направление: {data['direction']}
            💬 Комментарий: {data['comment']}"""

            await client.send_message(MANAGER_CONTACT, text)
            await message.reply("✅ Заявка отправлена менеджеру.")
            user_state.pop(user_id)

    @app.on_callback_query(filters.regex("^apply_dir_"))
    async def apply_dir(client, callback_query: CallbackQuery):
        user_id = callback_query.from_user.id
        direction = callback_query.data.split("_")[-1]
        user_state[user_id]["direction"] = direction
        user_state[user_id]["step"] = "comment"
        await callback_query.message.edit_text("💬 Добавьте комментарий (или напишите «-», если без комментария):")
