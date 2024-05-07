import logging  # модуль для сбора логов
from math import *  # математический модуль для округления
# подтягиваем константы из config файла
from config import *
import telebot
# подтягиваем функции для работы с БД
from F_database import *
# подтягиваем функцию для подсчета токенов в списке сообщений
from F_gpt import count_gpt_tokens
import  telebot
# настраиваем запись логов в файл
logging.basicConfig(filename=LOGS, level=logging.ERROR, format="%(asctime)s FILE: %(filename)s IN: %(funcName)s MESSAGE: %(message)s", filemode="w")

# получаем количество уникальных пользователей, кроме самого пользователя
def check_number_of_users(user_id):
    count = count_users(user_id)
    if count is None:
        return None, "Ошибка при работе с БД"
    if count > MAX_USERS:
        return None, "Превышено максимальное количество пользователей"
    return True, ""

# проверяем, не превысил ли пользователь лимиты на общение с GPT
def is_gpt_token_limit(messages, total_spent_tokens):
    all_tokens = count_gpt_tokens(messages) + total_spent_tokens
    if all_tokens > MAX_USER_GPT_TOKENS:
        return None, f"Превышен общий лимит GPT-токенов {MAX_USER_GPT_TOKENS}"
    return all_tokens, ""

#

def is_stt_block_limit(user_id, duration):
    # Задаем лимит продолжительности одного голосового сообщения
    single_message_limit = 30
    # Задаем общее количество блоков на пользователя
    total_blocks_limit = MAX_USER_STT_BLOCKS
    
    # Используем функцию count_all_limits для получения общего количества блоков пользователя
    total_blocks = count_all_limits(user_id, 'stt_blocks')
    
    # Проверяем, превышает ли продолжительность одного голосового сообщения заданный лимит
    if duration > single_message_limit:
        return True, "Ошибка: превышен лимит продолжительности одного голосового сообщения"
    
    # Проверяем, не превышает ли пользователь общее количество блоков
    if total_blocks >= total_blocks_limit:
        return True, "Ошибка: превышен общее количество блоков"
    
    return False, None


def is_tts_symbol_limit(user_id, text):
    # Задаем лимит количества символов
    symbol_limit = MAX_USER_TTS_SYMBOLS # Пример лимита, адаптируйте его под свои нужды
    
    # Используем функцию count_all_limits для получения общего количества символов пользователя
    total_symbols = count_all_limits(user_id, 'tts_symbols')
    
    # Проверяем, не превышает ли количество символов в тексте заданный лимит
    if len(text) + total_symbols > symbol_limit:
        return True, "Ошибка: превышен лимит символов"
    
    return False, None
    
