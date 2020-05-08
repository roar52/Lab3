import random
import Checker

from AbstractCrypt import Abstract
class Replacement(Abstract):
    def key_generator(self):
        alph_path=Checker.Checker.file_chek('alph','алфавитом')
        with open(alph_path,'r') as file:
            alph=[]
            for line in file:
                alph=line.split(',')
        keys=[]
        for i in range(len(alph)):
            keys.append(alph[i])

        random.shuffle(keys)

        key_dic={}
        for i in range(len(alph)):
            key_dic[alph[i]]=keys[i]
        while True:
            user_choice=input("Напечатать ключ? (Да/Нет)")
            if user_choice.lower()=="да":
                for key in key_dic:
                    print(key,"=",key_dic[key])
                break
            elif user_choice.lower()=="нет":
                break
            else:
                print('Неправильная команда! Попробуйте снова...')

        key_path = Checker.Checker.file_chek('key', 'ключом')

        crypt_name='replacement'
        for i in key_dic:
            crypt_name=crypt_name+','+i+':'+key_dic[i]

        with open(key_path,'w') as file:
            file.write(crypt_name)
            print('Ключ сохранен в файле:', key_path)


    def encrypt(self,text_path):
        key=self.__get_key()
        encrypt_text='replacement\n'
        with open(text_path,'r') as file:
            line=file.read()
            for i in range(len(line)):
                for j in key:
                    if line[i]==j:
                        encrypt_text+=key[j]
                        break

        with open (text_path+'.encrypt','w') as file:
            file.write(encrypt_text)
            print('Шифротекст сохранен в файле:',text_path,'.encrypt')

    def decrypt(self,text_path):
        key=self.__get_key()
        decrypt_text=''
        with open(text_path,'r') as file:
            checker=False
            for line in file:
                if line=='replacement\n':
                    checker=True
                break
            if checker:
                line=file.read()
                for i in range(len(line)):
                    for j in key:
                        if line[i]==key[j]:
                            decrypt_text+=j
                            break
                with open (text_path+'.txt','w') as file:
                    file.write(decrypt_text)
                    print('Расшифрованный текст сохранен в файле:', text_path, '.txt')
            else:
                print('Непраильный текст для расшифрования')





    def __get_key(self):
        dirty_key = []
        key_path = Checker.Checker.file_chek('key', 'ключом')
        with open(key_path, 'r') as file:
            for line in file:
                dirty_key=line.split(',')
                if dirty_key[0].lower() == 'replacement':
                    break
                else:
                    print('Неправильный ключ! Попробуйте снова')
        key = {}
        for i in range(1,len(dirty_key)):
            list=dirty_key[i].split(':')
            key[list[0]]=list[1]


        return key
