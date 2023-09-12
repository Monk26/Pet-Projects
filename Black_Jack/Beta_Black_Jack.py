from random import *
def play_Black_Jack():
    #input("начнём? - ") #"Виртуальная" кнопка
    print()
    all_cards=["2","3","4","5","6","7","8","9","Валет","Дама","Король","Туз"]
    sum=0
    your_cards=[]
    print("Ходы:")
    while sum<21:
        #input("Чтобы взять карту введите: <Карту> (без '<>') - ") #"Виртуальная" кнопка
        card=all_cards[randint(0,len(all_cards)-1)]
        your_cards.append(card)
        if card in all_cards[0:8]:
            sum+=int(card)
        if card in all_cards[8:11]:
            sum+=10
        if card=="Туз" and sum+11<=21:
            sum+=11
        if card=="Туз" and sum+11>21:
            sum+=1
        print("Ваша карта", card)
        print("Сумма:",sum)
        print()
    print("Итог:")
    if sum==21:
        your_cards=",".join(your_cards)
        print("Ты выйграл!!!")
        print("Ваши карты:",your_cards)
        print("Сумма:", sum)
    else:
        your_cards=", ".join(your_cards)
        print("Ты проиграл!!!")
        print("Ваши карты:",your_cards)
        print("Сумма:", sum)
        
play_Black_Jack()

#                ВЫВОД ОКНА
# from PyQt6.QtWidgets import QApplication, QWidget

# import sys 


# app = QApplication(sys.argv)


# window = QWidget()
# window.show()  


# app.exec()