
while True:
    menu = {'мафин': ["мука, вода, яйца, сахар", '10', "200gr"],
            'торт': ["мука, вода, яйца, сахар, сливки, крем", '15', "350gr"],
            'пироженное': ["мука, вода, яйца, сахар, сливки, крем", '15', "350gr"],
            'кофе': ["мука, вода, яйца, сахар, сливки, крем", '15', "350gr"],
            }

    a=input("1.название – описание\n"
            "2.название – цена.\n"
            "3.название – количество.\n"
            "4. Всю информацию. \n"
            "5. Приступить к покупке: С клавиатуры вводите название торта и его кол-во. \n"
            "n – выход из программы.\n")
    if a=='1':                                                          #при нажатии на кнопку 1
        print("Название и состав продукции")
        for i in menu:
            print("\n"+i+"\ncomposition:", menu.get(i)[0])
        print("\n***********************************************")
    elif a=='2':                                                        #при нажатии на кнопку 2
        print("Название и цена продукции")
        for i in menu:
            print("\n" + i + "\nPrice:", menu.get(i)[1]+"$")
        print("\n***********************************************")
    elif a=='3':                                                        #при нажатии на кнопку 3
        print("Название и количество продукции")
        for i in menu:
            print("\n" + i + "\nvalue:", menu.get(i)[2])
        print("\n***********************************************")
    elif a=='4':                                                            #при нажатии на кнопку 4
        print("Всё меню")
        for i in menu:
            print("\n" + i + "\ncomposition:", menu.get(i)[0]+"\n","Price:", menu.get(i)[1]+"$"+"\n","value:", menu.get(i)[2])
        print("\n***********************************************")
    elif a=='5':                                                    #при нажатии на кнопку 5
        buy={}
        while True:
            goods=input("Введите что хотите купить").lower()
            quantity=input("Введите количество этого товара")
            if menu.get(goods)!=None:                               #если товар есть в меню добавляем в
                buy.update({goods:[menu.get(goods)[1],quantity,]})  #словарь купленных товаров
                menu.pop(goods)                                     # и убираем из меню
            else:                                                   # в случае если в меню нет товара или он уже заказан
                print("такого товара нет\n вот что есть")           #выводим что есть
                for i in menu:
                    print("\n" + i)
                continue
            w=input("Хотите что-то ещё?\nда-ДА\nнет-нет")
            if w=='нет':
                break
        price=0
        for i in buy:                                           # выводим чек
            print("Вы купили ",buy.get(i)[1],i,)
            price+=int(buy.get(i)[0])*int(buy.get(i)[1])
        print("C вас ", price,"$")
    elif a=='n':
        break
    a=input("хотите продолжить? да/нет")
    if a=='нет':
        print("спасибо досвидания!")
        break
    elif a=='да':
        continue