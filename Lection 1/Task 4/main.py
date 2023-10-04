operation=input("Выберите операциб(+, -, *, /, корень, степень):")
if operation not in ('+', '-', '*', '/', 'корень', 'степень'):
    print("неверная операция")
else:
    if operation in ('корень', 'степень'):
        num=float(input("введите число:"))
    else:
        num1=float(input("Число 1, "))
        num2=float(input("Число 2, "))

    if operation=='+':
        result=num1+num2
    elif operation=='-':
        result=num1-num2
    elif operation=='*':
        result=num1*num2
    elif operation=='/':
        if num2==0:
            result="Деление на 0 невозможно"
        else:
            result=num1/num2
    elif operation=='корень':
        if num<0:
            result="нельзя извлеч корень из отрецательного числа"
        else:
            result=num**0.5
    elif operation =='степень':
        result=num1**num1
    print("результат", result)