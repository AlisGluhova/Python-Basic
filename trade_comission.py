city = input()
sales = float(input())
if city == 'Sofia':
    if 0 <= sales <= 500:
        commission = f'{sales * 0.05:.2f}'
        print(commission)
    elif 500 <= sales <= 1000:
        commission = f'{sales * 0.07:.2f}'
        print(commission)
    elif 1000 <= sales <= 10000:
        commission = f'{sales * 0.08:.2f}'
        print(commission)
    elif sales >= 10000:
        commission = f'{sales * 0.12:.2f}'
        print(commission)
    else:
        print(f'error')
elif city == 'Varna':
    if 0 <= sales <= 500:
        commission = f'{sales * 0.045:.2f}'
        print(commission)
    elif 500 <= sales <= 1000:
        commission = f'{sales * 0.075:.2f}'
        print(commission)
    elif 1000 <= sales <= 10000:
        commission = f'{sales * 0.1:.2f}'
        print(commission)
    elif sales >= 10000:
        commission = f'{sales * 0.13:.2f}'
        print(commission)
    else:
        print(f'error')
elif city == 'Plovdiv':
    if 0 <= sales <= 500:
        commission = f'{sales * 0.055:.2f}'
        print(commission)
    elif 500 <= sales <= 1000:
        commission = f'{sales * 0.08:.2f}'
        print(commission)
    elif 1000 <= sales <= 10000:
        commission = f'{sales * 0.12:.2f}'
        print(commission)
    elif sales >= 10000:
        commission = f'{sales * 0.145:.2f}'
        print(commission)
    else:
        print(f'error')
else:
    print(f'error')
