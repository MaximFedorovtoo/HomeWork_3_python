
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
def emptiness():
    print(' ')
    print(' ')


def task_1():
    print ('Задача 16')
    emptiness()
    array = []
    while len(array)+1 > 0:
        temp = input('Введите переменную массива либо введите q: ')
        if temp == 'q':
            break
        array.append(int(temp))
    N = int(input('Введите число которое будете искать '))
    temp = 0
    for i in range(len(array)):
        if array[i] == N:
            temp+=1
    if temp == 0:
        print(f'Число {N} отсутствует в массиве')
    else:
        print(f'Число {N} встречается в массиве {array} -> {temp} раз')


        

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

def task_2():
    print ('Задача 18')
    emptiness()
    array = []
    while len(array)+1 > 0:
        temp = input('Введите переменную массива либо введите "q": ')
        if temp == 'q':
            break
        array.append(int(temp))
    N = int(input('Введите число к которому будете искать самый близкий по величине элемент'))
    num = array[0]
    for i in range(len(array)):
        if array[i] < N and array[i] > num:
             num = array[i]
    print(f'Ближайшее число {num}')



# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
#  D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
#  А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка;
#  Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. Будем считать,
#  что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12
def task_3():
    print ('Задача 20')
    emptiness()

    # one_point_array = ['A', 'E', 'I', 'O','U', 'L', 'N,' 'S', 'T', 'R' ,'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т' ]
    # two_poin_array = ['D', 'G','Д', 'К', 'Л', 'М', 'П', 'У' ]
    # three_poit_array = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
    # five_poit_array = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
    # egtht_poit_array = ['J', 'X', 'Ш', 'Э', 'Ю']
    # ten_poit_array = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']
    enter_word = input('Ведите слово: ').upper()
    # count = 0

    # for i in range(len(enter_word)):
    #     if str.upper(enter_word[i]) in one_point_array:
    #         count +=1
    #     if str.upper(enter_word[i])in two_poin_array:
    #         count +=2
    #     if str.upper(enter_word[i]) in three_poit_array:
    #         count +=3
    #     if str.upper(enter_word[i]) in five_poit_array:
    #         count +=5
    #     if str.upper(enter_word[i]) in egtht_poit_array:
    #         count +=8
    #     if str.upper(enter_word[i]) in ten_poit_array:
    #         count +=10
    # print(f'Вы получили {count}')

    scrable = {1:['A', 'E', 'I', 'O','U', 'L', 'N,' 'S', 'T', 'R' ,'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
               2:['D', 'G','Д', 'К', 'Л', 'М', 'П', 'У' ],
                3:['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'],
                 5:['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'],
                  8:['J', 'X', 'Ш', 'Э', 'Ю'],
                   10:['Q', 'Z', 'Ф', 'Щ', 'Ъ']}
    point = 0
    for i in enter_word:
        for j in scrable:
            if i in scrable[j]:
                point = point + j
                
    print(point)
        
def main():
    task_1()
    emptiness()
    task_2()
    emptiness()
    task_3()



if __name__ == '__main__':
    main()