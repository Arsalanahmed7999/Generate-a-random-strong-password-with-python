while True:
    import random
    print('Generate your password!')

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNOPQRSTUVWXYZ!@#$%^&*()><.,/-01234567890'

    numbers = int(input('Enter the number of time you want to generate the password: \n'))

    length = int(input('Enter the length of the password: \n'))

    for pwd in range(numbers):
        passwords = ''
        for i in range(length):
            passwords+=random.choice(chars)
        print(passwords)
    wantToQuit = input('Do you want to quit: (yes/no) \n')
    if wantToQuit == 'yes':
        break


