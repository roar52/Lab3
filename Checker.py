import json
class Checker:

    @staticmethod
    def __path_check(file_path,file_expansion):
            key_check = file_path.split('.')
            if key_check[len(key_check) - 1] == file_expansion:
               return True
            return False

    @staticmethod
    def __file_exist(file_path,do):
        try:
           file=open(file_path,do)
        except FileNotFoundError:
            print('Не существует такого файла! Попробуйте снова')
            return False
        else:
            return True

    @staticmethod
    def file_chek(expansion,type,do):
        while (True):
            file_path = (input(f'Укажите файл с {type}:'))
            alph_check = Checker.__path_check(file_path, expansion)
            if alph_check:
                if do=='r':
                    if Checker.__file_exist(file_path,do):
                        break
                elif do=='w':
                    if Checker.__file_exist(file_path,do):
                        break
            else:
                print(f'Неправильное расширение файла с {type}! Попробуйте снова')

        return file_path

    @staticmethod
    def get_info_from_json(file_path):
        try:
            with open(file_path, 'r') as file:
                text = json.load(file)
        except json.decoder.JSONDecodeError:
            print('Неправильная информация в файле! Попробуйте снова')
            return False
        else:
            return True

    @staticmethod
    def value_check(text):
        while True:
            try:
                user_value=int(input(text))
            except ValueError:
                print("Неверный тип данных! Попробуйте снова")
            else:
                if user_value>=1:
                    return user_value
                else:
                    print('Неправильные данные! Попробуйте снова')

    @staticmethod
    def alph_check(alph):
        alph_twice=[]
        for i in range(len(alph)):
            if not(alph[i] in alph_twice):
                alph_twice.append(alph[i])
            else:
                return False

        return True