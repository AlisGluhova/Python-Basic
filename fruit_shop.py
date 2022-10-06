fruit=input()
day=input()
quantity=float(input())
price=0
if day=='Monday' or day=='Tuesday' or day=='Wednesday' or day=='Thursday' or day=='Friday':
    if fruit=='banana':
        price=f'{2.50*quantity:.2f}'
        print(price)
    elif fruit=='apple':
        price=f'{1.20*quantity:.2f}'
        print(price)
    elif fruit=='orange':
        price=f'{0.85*quantity:.2f}'
        print(price)
    elif fruit=='grapefruit':
        price=f'{1.45*quantity:.2f}'
        print(price)
    elif fruit=='kiwi':
        price=f'{2.70*quantity:.2f}'
        print(price)
    elif fruit=='pineapple':
        price=f'{5.50*quantity:.2f}'
        print(price)
    elif fruit=='grapes':
        price=f'{3.85*quantity:.2f}'
        print(price)
    else:
        print(f'error')
elif day=='Saturday' or day=='Sunday':
    if fruit=='banana':
        price=f'{2.70*quantity:.2f}'
        print(price)
    elif fruit=='apple':
        price=f'{1.25*quantity:.2f}'
        print(price)
    elif fruit=='orange':
        price=f'{0.90*quantity:.2f}'
        print(price)
    elif fruit=='grapefruit':
        price=f'{1.60*quantity:.2f}'
        print(price)
    elif fruit=='kiwi':
        price=f'{3.00*quantity:.2f}'
        print(price)
    elif fruit=='pineapple':
        price=f'{5.60*quantity:.2f}'
        print(price)
    elif fruit=='grapes':
        price=f'{4.20*quantity:.2f}'
        print(price)
    else:
        print(f'error')
else:
    print(f'error')
