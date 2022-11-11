from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_welcome_btn = InlineKeyboardButton('Продолжить', callback_data='welcome_btn')
inline_welcome_kb = InlineKeyboardMarkup().add(inline_welcome_btn)

inline_link_to_questionnaire_btn = InlineKeyboardButton('', url='https://vk.com/audio-2001775534_63775534')
inline_link_to_questionnaire_kb = InlineKeyboardMarkup().add(inline_link_to_questionnaire_btn)
