from API_settings import *                                  # Из файла с настройками берём вообще всё (библиотеки тоже)


class Quote(Resource):                                      # Класс для отправки/получения запросов
    def get(self, variation=0, user_id=0, product_id=0):    # HTTP-запрос типа GET
        if variation == 0:
            pass
        elif variation == 1:
            pass
        elif variation == 2:
            pass

