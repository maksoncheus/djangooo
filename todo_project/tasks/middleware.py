import logging
import os
from datetime import datetime

# Получаем путь к лог-файлу из переменной окружения
# Если переменная не задана, по умолчанию используется 'default.log'
log_file_path = os.environ.get('LOG_FILE_PATH', 'default.log')

# Настраиваем логгер
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - IP: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Получаем IP-адрес клиента
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        
        # Записываем информацию в лог
        logging.info(ip)

        response = self.get_response(request)
        return response
