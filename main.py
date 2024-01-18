for number in range(1, 101):
    count = 0

    for contador in range(1, number+1):
        if number % contador == 0:
            count += 1

    if count < 3:
        print(f'{number} --> PRIMO')
    else:
        print(f'{number} --> NÃO É PRIMO')
