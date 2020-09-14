import random

input('Enter the name: ')
input('Enter the surname: ')
input('Enter the age: ')
input('Enter the class: ')
count_true = 0
count_false = 0
count = 0
text_ela = ['Ela, Sukani bele saxla!!!', 'Netice superdi, amma arxayin olma daha da yaxsiya dogru get']
text_kafi = ['Pis deyil amma netice bundan da yaxsi ola biler', 'Bir sonrakina mutleq daha yaxsi ol!!!']
text_pis = ['Hevesden dusmeden oz uzerinde calismalisan', 'Tomas Edison bele lampa ixtira ederken 10 000 defe yoxlayib... Sen de bir daha yoxla. Mutleq ki alinacaq!']
while True:
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    op = random.randint(1, 2)

    if op == 1:
        print(a, '+', b, '=')
        n = int(input('enter the answer: '))
        if n == "q":
            break

        if a + b == n:
            print('Duzdur')
            count_true = count_true + 1
        if a + b != n:
            print('Sehvdir')
            count_false = count_false + 1
    if op == 2:
        if a > b:
            print(a, '-', b, '=')
            n = int(input('enter the answer: '))
            if a - b == n:
                print('Duzdur')
                count_true = count_true + 1
            if a - b != n:
                print('Sehvdir')
                count_false = count_false + 1
        else:
            print(b, '-', a, '=')
            n = int(input('enter the answer: '))
            if b - a == n:
                print('Duzdur :) ')
                count_true = count_true + 1
            if b - a != n:
                print('SEHVDIIIIRRR!!!!')
                count_false = count_false + 1

    count = count + 1
    if count % 5 == 0:
        s = input('do you want to exit? y/n: ')
        if s == 'y':
            print("Sehvlerin Sayi: ", count_false)
            print("Duzlerin sayi: ", count_true)
            if count_false == 0:
                print(random.choice(text_ela))
            elif count_true > count_false:
                print(random.choice(text_kafi))
            else:
                print(random.choice(text_pis))

            break
