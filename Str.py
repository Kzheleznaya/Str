# строки могут заключаться как в двойные, так и в одинарные ковычки. Пример:
str1 = "Hey."
str2 = 'Whats up?'
print(str1)
print(str2)
'''Операции сложения и умножения'''
fullstr= str1 +""+str2   # сложение через доп переменнную
print(fullstr)
print(str1 + str2)       # сложение через функцию print
print('@'+str1)
print(str1 *10)          # умножение переменной str1 10 раз
print("@" * 50)          # умножение без создания доп переменной
# Какие типы данных можно преобразовать в строку:
ex= 123
print(type(ex))
ex1= str(ex)
print(type(ex1))
# по примеру из видео урока
print(len(str2))
print(str2.title())
print(str2.capitalize())
print(str2.upper())
print(str2.lower())
print(str2.isupper())
print(str2.islower())
print(str2.index('t'))
print(str2.find('u'))


