#simple calculater using the dict
def basicCalculator(operator,num1,num2):
    return{
        'add': lambda: num1 + num2,
        'div': lambda: num1 / num2,
        'mul': lambda: num1 * num2,
        'sub': lambda: num1 - num2,
        }.get(operator,lambda: None)()


print(basicCalculator('mul',2,10))