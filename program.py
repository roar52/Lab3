import Replacment,Transposition,Gamming
import Checker
def print_main_menu():
    print("-> Главное меню:")
    print('->   1) Зашифровать/Расшифровать')
    print('->   2) Сгенерировать ключ')
    print('->   3) Выход')

def crypt_menu():
    print('->Зашифровать/Расшифровать:')
    print('->	1) Зашифровать')
    print('-> 	2) Расшифровать')

def second_crypt_menu():
    print('-> 	1) Применить шифр заменой')
    print('-> 	2) Применить шифр перестановкой')
    print('-> 	3) Применить шифр гаммирование')

replace=Replacment.Replacement()
transpos=Transposition.Transposition()
gamming=Gamming.Gamming()


while True:
    print_main_menu()
    main_menu_choice=input('-> Ваш выбор: ')
    if main_menu_choice=='1':
        crypt_menu()
        menu_choice=input('-> Ваш выбор: ')
        if menu_choice=='1':
            second_crypt_menu()
            while True:
                user_choice = input('-> Ваш выбор: ')
                if user_choice=='1':
                    text_path=Checker.Checker.file_chek('txt','текстом','r')
                    replace.encrypt(text_path)
                    break
                elif user_choice=='2':
                    text_path=Checker.Checker.file_chek('txt','текстом','r')
                    transpos.encrypt(text_path)
                    break
                elif user_choice=='3':
                    text_path=Checker.Checker.file_chek('txt','текстом','r')
                    gamming.encrypt(text_path)
                    break
                else:
                    print('Неверная команда! Попобуйте снова')
        elif menu_choice=='2':
            second_crypt_menu()
            while True:
                user_choice = input('-> Ваш выбор: ')
                if user_choice=='1':
                    text_path=Checker.Checker.file_chek('encrypt','шифртекстом','r')
                    replace.decrypt(text_path)
                    break
                elif user_choice=='2':
                    text_path=Checker.Checker.file_chek('encrypt','шифртекстом','r')
                    transpos.decrypt(text_path)
                    break
                elif user_choice=='3':
                    text_path=Checker.Checker.file_chek('encrypt','шифртекстом','r')
                    gamming.decrypt(text_path)
                    break
                else:
                    print('Неверная команда! Попобуйте снова')
    elif main_menu_choice=='2':
        print('Ввыберите метод для которго сгенерировать ключ')
        print('->   1) метод замены')
        print('->   2) метод перестановки')
        print('->   3) метод гаммирование')
        while True:
            user_choice=input('-> Ваш выбор: ')
            if user_choice=='1':
                replace.key_generator()
                break
            elif user_choice=='2':
                transpos.key_generator()
                break
            elif user_choice=='3':
                gamming.key_generator()
                break
            else:
                print('Неверная команда! Попобуйте снова')
    elif main_menu_choice=='3':
        break
    else:
        print('Неверная команда! Попобуйте снова')