


# def sum():
#     a=5
#     b=6
#     print('Sum numbers...')
#     c = a+b
#     print('Result...' + str(c))

# sum()

def yourname(name:str):
     print(name)

# yourname('Ernesto')

def sum(a:int, b:int, c:int):
    print('Result...'+str(a+b+c))

# sum(1,2,3)

def operations(a:int, b:int, op:str='*'):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        return a/b

n = operations(b=5,a=2, op='-')
print('Resultado...'+str(n))
    