import random,Checker,json
from AbstractCrypt import Abstract
class Transposition(Abstract):
    def key_generator(self):
        user_len=Checker.Checker.value_check('Укажите размер блока перестановки: ')
        key=[]
        for i in range(1 ,user_len+1):
            key.append(i)
        random.shuffle(key)
        while True:
            user_choice=input('Напечатать ключ?(Да/Нет): ')
            if user_choice.lower()=='да':
                print(key)
                break
            elif user_choice.lower()=='нет':
                break
            else:
                print('Неправильная команда! Попробуйте снова')

        key = ['transposition'] + key
        key_path=Checker.Checker.file_chek('key','ключом','w')
        with open(key_path,'w') as file:
            json.dump(key,file,ensure_ascii=False)
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
        text_path=text_path+'.encrypt'
        with open(text_path,'w') as file:
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
                text_path=text_path+'.txt'
                with open(text_path,'w') as file:
                    file.write(decrypt_text)
                    print('Расшифрованный текст сохранен в файле:', text_path, '.txt')
            else:
                print('Непраильный текст для расшифрования')

    def __get_key(self):
        while True:
            key_path=Checker.Checker.file_chek('key','ключом','r')
            if Checker.Checker.get_info_from_json(key_path):
                with open(key_path, 'r') as file:
                    dirty_key = json.load(file)
                    if dirty_key[0].lower() == 'transposition':
                        key = []
                        for i in range(1, len(dirty_key)):
                            key.append(int(dirty_key[i]))
                        return key
                    else:
                        print('Неправильный ключ! Попробуйте снова')



