from API_settings import *                                  # Вся основа API и библиотеки из файла с настройками


class Quote(Resource):                                      # Класс для обработки запросов
    def get(self, variation=0, user_id=0, product_id=0):    # Метод GET HTTP-запроса
        if variation == 0:                                  # Вывод информации о покупателе
            pass
        elif variation == 1:                                # Вывод информации о продавце
            pass
        elif variation == 2:                                # Вывод информации о товаре
            pass
