TOKEN = '6842648079:AAFB4yZgwkM6WHt7LhLkDcWmDBZfU2JpG0A'  # token телеграм-бота
IAM_TOKEN = 't1.9euelZrHl8ubycmPlpCVmI6Rz8yPl-3rnpWaj8jHjJ7OkZjPm4-NyZqTlcfl8_crIxdO-e8eOlo-_t3z92tRFE757x46Wj7-zef1656Vms6SmZbNlJidyZKcjo6bl8yd7_zF656Vms6SmZbNlJidyZKcjo6bl8ydveuelZqeyZSOiZCLy5PLjYnPk5SakrXehpzRnJCSj4qLmtGLmdKckJKPioua0pKai56bnoue0oye.1YWoxHTtCQhN6Oh5Ldnj9T4QTOEM6YZe83la28ue2IZ8kLd0oM7JdWJcZUu_XLN9NQkwwOzXBl-YbTqaNMv2Bw'
FOLDER_ID = 'b1gh50dain42smatakvf'
MAX_USERS = 3  # максимальное кол-во пользователей
MAX_GPT_TOKENS = 120  # максимальное кол-во токенов в ответе GPT
COUNT_LAST_MSG = 4  # кол-во последних сообщений из диалога

# лимиты для пользователя
MAX_USER_STT_BLOCKS = 10  # 10 аудиоблоков
MAX_USER_TTS_SYMBOLS = 5_000  # 5 000 символов
MAX_USER_GPT_TOKENS = 2_000  # 2 000 токенов

LOGS = 'logs.txt'  # файл для логов
DB_FILE = 'messages.db'  # файл для базы данных
SYSTEM_PROMPT = [{'role': 'system', 'text': 'Ты веселый собеседник. Общайся с пользователем на "ты" и используй юмор. '
                                            'Поддерживай диалог. Не объясняй пользователю, что ты умеешь и можешь. '
                                            'Изображай человека'}]  # список с системным промтом