from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_lang_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
         InlineKeyboardButton("🇰🇬 Кыргызча", callback_data="lang_kg")]
    ])

def get_main_menu(lang):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Направления", callback_data="directions")],
        [InlineKeyboardButton("📋 Как поступить", callback_data="admission")],
        [InlineKeyboardButton("📞 Связаться", callback_data="contact")],
        [InlineKeyboardButton("📝 Подать заявку", callback_data="apply")],
        [InlineKeyboardButton("🎥 Видео-обзор", callback_data="video")],
        [InlineKeyboardButton("🗺️ Как найти нас", callback_data="location")],
        [InlineKeyboardButton("❓ Частые вопросы", callback_data="faq")]
    ])

def get_back_menu(lang):
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Назад", callback_data="back")]])

def get_directions_menu(lang):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Full Stack 👨‍💻", callback_data="dir_fullstack")],
        [InlineKeyboardButton("Мобильная 📱", callback_data="dir_mobile")],
        [InlineKeyboardButton("Робототехника 🤖", callback_data="dir_robot")],
        [InlineKeyboardButton("Мехатроника 🔧", callback_data="dir_mech")],
        [InlineKeyboardButton("Автоэлектрик 🚗", callback_data="dir_auto")],
        [InlineKeyboardButton("🔙 Назад", callback_data="back")]
    ])

def get_apply_direction_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Full Stack", callback_data="apply_dir_fullstack")],
        [InlineKeyboardButton("Мобильная", callback_data="apply_dir_mobile")],
        [InlineKeyboardButton("Робототехника", callback_data="apply_dir_robot")],
        [InlineKeyboardButton("Мехатроника", callback_data="apply_dir_mech")],
        [InlineKeyboardButton("Автоэлектрик", callback_data="apply_dir_auto")]
    ])
