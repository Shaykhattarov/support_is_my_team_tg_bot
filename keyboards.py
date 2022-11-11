from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_link_to_questionnaire_btn = InlineKeyboardButton('Продолжить', url='https://docs.google.com/forms/d/e/1FAIpQLSfX8Cqpz4Q5rpJILvq7K0j2_2PT9HkevEpR0jJ7-um5TADcgw/viewform?usp=sharing')
inline_link_to_questionnaire_kb = InlineKeyboardMarkup().add(inline_link_to_questionnaire_btn)
