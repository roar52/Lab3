class Checker:

    @staticmethod
    def __path_check(file_path,file_expansion):
            key_check = file_path.split('.')
            if key_check[len(key_check) - 1] == file_expansion:
               return True
            return False

    @staticmethod
    def __file_exist(file_path):
        try:
           file=open(file_path,'r')
        except FileNotFoundError:
            print('Не существует такого файла! Попробуйте снова')
            return False
        else:
            return True

    @staticmethod
    def file_chek(expansion,type,do):
        while (True):
            alph_path = (input(f'Укажите файл с {type}:'))
            alph_check = Checker.__path_check(alph_path, expansion)
            if alph_check:
                if do=='r':
                    if Checker.__file_exist(alph_path):
                        break
                break
            else:
                print(f'Неправильное расширение файла с {type}! Попробуйте снова')

        return alph_path