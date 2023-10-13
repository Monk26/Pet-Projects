from random import *
from termcolor import colored
# from PyQt6.QtWidgets import QApplication, QWidget

# import sys 


# app = QApplication(sys.argv)
# window = QWidget()
# window.show()  
# app.exec()




def play_Black_Jack():
    input("Начнём? - ") #"Виртуальная" кнопка
    
    print()
    
    all_cards={"2" : 2, "3" : 3,"4" : 4,"5" : 5,"6" : 6, "7": 7, "8" : 8 ,"9" : 9, "10" : 10 , "Валет" : 10, "Дама" : 10, "Король" : 10, "Туз" : 11}
    sum=0
    your_cards=list()
    card=""
    
    print("Ходы:")
    
    input("Чтобы взять карту введите: <Карту> (без '<>') - ") #"Виртуальная" кнопка
    while sum<21:
        card = choice(list(all_cards.keys()))

        if card == "Туз":
            if (sum + int(all_cards[card])) <= 21:
                sum += all_cards[card]
            else:
                sum += 1
        else:
            sum += all_cards[card]
        
        your_cards.append(card)
        print("Ваша карта", card)
        print("Сумма:", sum)
        print()
        if "нет" in input("Если хотите закончить, то введите <Нет>, иначе введите <Да>: ").lower() or sum>=21:
            break
        
    print("Итог:")
    
    if sum==21:
        your_cards = ", ".join(your_cards)
        print(colored("Ты выйграл!!!", "green"))
        print("Ваши карты:",your_cards)
        print("Сумма:", sum)
        
    else:
        your_cards=", ".join(your_cards)
        print(colored("Ты проиграл!!!", "red"))
        print("Ваши карты:",your_cards)
        print("Сумма:", sum)
        
play_Black_Jack()

