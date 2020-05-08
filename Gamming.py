import Checker,random
from AbstractCrypt import Abstract

class Gamming(Abstract):
    def __init__(self):
        self.__alph={}
        self.__module=0
    def key_generator(self):
        alph_path=Checker.Checker.file_chek('alph','алфавитом')

        file=open(alph_path)
        line=file.read()
        alph = line.split(',')
        self.__module=len(alph)
        index=int(input('Введите индекс первой буквы в алфавите: '))

        dic = {}
        for i in range(len(alph)):
            dic[alph[i]] = i+index
        self.__alph=dic
        while True:
            gamma_len=int(input('Введите длину гаммы: '))
            if gamma_len<1:
                print('Неправильная длина гаммы!')
            else:
                break
        key=[]
        for i in range(gamma_len):
            gamma_elem = int(input(f'Введите {i + 1} элемент гаммы: '))
            key.append(gamma_elem)
        while (True):
            user_choice = input("Напечатать ключ? (Да/Нет)")
            if user_choice.lower() == "да":
                key_text = ''
                for i in range(len(key)):
                    if (i == len(key) - 1):
                        key_text += str(key[i])
                    else:
                        key_text += str(key[i]) + ','
                print(key_text)
                break
            elif user_choice.lower() == "нет":
                break
            else:
                print('Неправильная команда! Попробуйте снова...')
        key_path = Checker.Checker.file_chek('key', 'ключом')

        crypt_name = 'gamming'
        for i in range(len(key)):
            crypt_name = crypt_name + ',' + str(key[i])

        with open(key_path, 'w') as file:
            file.write(crypt_name)
            print('Ключ сохранен в файле:', key_path)


    def encrypt(self,text_path):
        key=self.__get_key()
        encrypt_text='gamming\n'
        gamma_len=len(key)
        alph=self.__alph
        file=open(text_path)
        line=file.read()
        text_len=len(line)
        key_text = []
        for i in range(text_len // gamma_len):
            for symb in key:
                key_text.append(symb)
            for i in range(text_len % gamma_len):
                key_text.append(key[i])

        for i in range(text_len):
            check=False
            for j in self.__alph:
                if(j==line[i]):
                    index=(alph[j]+key_text[i])%self.__module
                    for k in alph:
                        if index==alph[k]:
                            encrypt_text += k
                            break
                    check=True
                    break
            if check==False:
                encrypt_text+=line[i]
        file.close()
        with open (text_path+'.encrypt','w') as file:
            file.write(encrypt_text)
            print('Шифротекст сохранен в файле:', text_path, '.encrypt')

    def decrypt(self,text_path):
        key = self.__get_key()
        decrypt_text = ''
        gamma_len = len(key)
        alph = self.__alph
        with open(text_path, 'r') as file:
            checker = False
            for line in file:
                if line == 'gamming\n':
                    checker = True
                break
            if checker:
                line = file.read()
                text_len = len(line)
                key_text = []
                for i in range(text_len // gamma_len):
                    for symb in key:
                        key_text.append(symb)
                    for i in range(text_len % gamma_len):
                        key_text.append(key[i])

                for i in range(text_len):
                    check = False
                    for j in self.__alph:
                        if (j == line[i]):
                            index = (alph[j] - key_text[i]+self.__module) % self.__module
                            for k in alph:
                                if index == alph[k]:
                                    decrypt_text += k
                                    break
                            check = True
                            break
                    if check == False:
                        decrypt_text += line[i]
                with open(text_path + '.txt', 'w') as file:
                    file.write(decrypt_text)
                    print('Расшифрованный текст сохранен в файле:', text_path, '.txt')
            else:
                print('Непраильный текст для расшифрования')

    def __get_key(self):
        key_path = Checker.Checker.file_chek('key', 'ключом')
        file=open(key_path)
        line=file.read()
        dirty_key = line.split(',')
        if dirty_key[0].lower() == 'gamming':
            key = []
            for i in range(1, len(dirty_key)):
                key.append(int(dirty_key[i]))
        else:
            print('Неправильный ключ! Попробуйте снова')

        return key

