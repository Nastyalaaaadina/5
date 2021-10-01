n=int(input('Введите число:'))
if not [x for x in str(n) if int(x) % 2]:
 print('Ошибка,ваше число НЕ содежит нечетные цифры,попробуйте еще раз.')
else: 
 print(min(int(x) for x in str(n) if int(x) % 2))