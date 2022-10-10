hour = int(input())
day = input()
if 10 <= hour <= 18 and (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day=='Saturday'):
    print(f'open')
else:
    print(f'closed')
