 # Учитывая целое число, 
 # вернуть количество шагов,
 # чтобы уменьшить его до нуля. 

# За один шаг,
# если текущее число четное,
# вы должны разделить его на 2,
# в противном случае
# вы должны вычесть из него 1.

# сложность - O(1) - множество

class Solution(object):
    def numberOfSteps(num: int):        #принимаем число int
        s = 0                           #добавляем шаг
        while num > 0:                  
            if num % 2: num -= 1        #если число нечетное (делится на 2 без остатка), вычетаем 1
            else: num // 2              #если число четное, делим на 2
            s += 1                      #прибавляем шаг
        return s                        #прибавляем шаг
    print(numberOfSteps(11)) 
