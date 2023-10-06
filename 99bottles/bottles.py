def bottles(num):
    original_num = num
    while (num > 1):
        print(f'{num} bottles of beer on the wall, {num} bottles of beer.')
        num-= 1
        if num == 1:
            print(f'Take one down and pass it around, {num} bottle of beer on the wall.')
        else:
            print(f'Take one down and pass it around, {num} bottles of beer on the wall.')
    print(f'1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, {original_num} bottles of beer on the wall.')

bottles(72)