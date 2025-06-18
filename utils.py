user_langs = {}

def set_user_lang(user_id, lang):
    user_langs[user_id] = lang

def get_user_lang(user_id):
    return user_langs.get(user_id, "ru")
