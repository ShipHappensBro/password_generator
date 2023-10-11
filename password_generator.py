import secrets
import string
from datetime import datetime
import os
import pyperclip

class crypted():
    def __init__(self,length) -> None:
        self.length=length

    def __str__(self) -> str:
        return("Пароль создан и скопирован в буфер обмена")
    
    def generate(self)->str:
        """
        Генерирует пароль с улучшенным шифрованием
        Возвращает str с информацией
        """
        letters_and_digits=string.ascii_letters + string.digits + string.punctuation
        crypt_rand= ''.join(secrets.choice(letters_and_digits) for element in range(self.length))
        self.copy_to_buffer(crypt_rand)
        return(self.write_to_txt(crypt_rand))
    
    def write_to_txt(self,password)->str:
        """
        """
        message=f'| Пароль: {password}  | Создан {datetime.today()} | Пользователем {os.getlogin()} |\n'
        try:
            with open('passwords.txt',"a+",encoding='utf-8') as file:
                file.write(message)
            print(self.__str__())
            return(message)
        except:
            exit(0)
    
    def copy_to_buffer(self,message)->None:
        """
        Копирует пароль в буфер обмена
        """
        pyperclip.copy(message)

    def open_explorer(self)->None|int:
        """
        Открывает txt с паролем
        """
        try:
            os.system(f"explorer.exe {os.curdir}\\passwords.txt")
        except:
            return(0)

if __name__=="__main__":
    print('Введите длину пароля')
    inputed_lenght=input()
    try:
        inputed_lenght=int(inputed_lenght)
    except:
        print('Введено не число')
        exit()
    start=crypted(inputed_lenght)
    start.generate()
    start.open_explorer()