#Последовательность Трибоначчи T n определяется следующим образом: 

#T 0 = 0, T 1 = 1, T 2 = 1 и T n+3 = T n + T n+1 + T n+2 для n >= 0.

#Учитывая n, вернуть значение T n .


def tribonacci(n: int) -> int:

    #Для первых трех значений n равно по условию

    if n == 0: # n-нное число
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    #Для остальных - пройдемся рекурсивной ф-цией

    arr = [0] * (n + 1) #cгенерируем кортеж 
    arr[1] = 1
    arr[2] = 1

    #Начиная с 3 числа n - вернем все значения n

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
        return arr[-1]

 



