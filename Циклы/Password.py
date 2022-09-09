pass1 = input()
pass2 = input()
a = 0
while a == 0:
    if len (pass1) < 8:
        print ('Короткий!')
        pass1 = input()
        pass2 = input()
    elif '123' in pass1:
        print ('Простой!')
        pass1 = input()
        pass2 = input()
    elif pass1 != pass2:
        print ('Различаются!')
        pass1 = input()
        pass2 = input()
    else:
        print ('ОК')
    a += 2
    