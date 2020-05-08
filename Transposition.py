import random,Checker
from AbstractCrypt import Abstract
class Transposition(Abstract):
    def key_generator(self):
        user_len=int(input('Укажите размер блока перестановки: '))
        key=[]
        for i in range(1 ,user_len+1):
            key.append(i)
        random.shuffle(key)
        key_s=''
        for i in range(len(key)):
            key_s += str(key[i])+','
        while True:
            user_choice=input('Напечатать ключ?(Да/Нет): ')
            if user_choice.lower()=='да':
                print(''.join(key))
                break
            elif user_choice.lower()=='нет':
                break
            else:
                print('Неправильная команда! Попробуйте снова')

        key_path=Checker.Checker.file_chek('key','ключом')
        with open(key_path,'w') as file:
            key_s='transposition,'+key_s
            file.write(key_s)
            print('Ключ сохранен в файле:',key_path)

    def encrypt(self,text_path):
        key=self.__get_key()
        encrypt_text = 'transposition\n'
        blockSize = len(key)
        with open(text_path, 'r') as file:
            line=file.read()

            text=line
            text_size=len(text)
            mod=text_size%blockSize
            if mod!=0:
                for k in range(blockSize-mod):
                    text+='z'
            for i in range(0,len(text),blockSize):
                transposition=list(range(len(key)))
                for j in range(len(key)):
                    transposition[key[j]-1]=text[i+j]
                for j in range(len(key)):
                    encrypt_text+=transposition[j]

        with open(text_path+'.encrypt','w') as file:
            file.write(encrypt_text)
            print('Шифротекст сохранен в файле:',text_path,'.encrypt')


    def decrypt(self,text_path):
        key=self.__get_key()
        blockSize = len(key)
        with open(text_path,'r') as file:
            checker = False
            for line in file:
                if line == 'transposition\n':
                    checker = True
                break
            if checker:
                decrypt_text=''
                text = file.read()
                text_size = len(text)
                for i in range(0, len(text), blockSize):
                    transposition = list(range(len(key)))
                    for j in range(len(key)):
                        transposition[j] = text[i+key[j]-1]
                    for j in range(len(key)):
                        decrypt_text += transposition[j]
                with open(text_path+'.txt','w') as file:
                    file.write(decrypt_text)
                    print('Расшифрованный текст сохранен в файле:', text_path, '.txt')
            else:
                print('Непраильный текст для расшифрования')

    def __get_key(self):
        dirty_key = []
        key_path=Checker.Checker.file_chek('key','ключом')
        with open(key_path, 'r') as file:
            for line in file:
                dirty_key = line.split(',')
                if dirty_key[0].lower() == 'transposition':
                    break
                else:
                    print('Неправильный ключ! Попробуйте снова')
        key = []
        for i in range(1, len(dirty_key)-1):
            key.append(int(dirty_key[i]))

        return key
