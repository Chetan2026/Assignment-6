def pangram(string):
    for i in range(65,91) :
        if chr(i) and chr(i).lower() in string :
            continue
        else :
            return False

string = str(input('enter a string :'))

a = pangram(string)

if a == False :
    print('It is not a pangram.')
else :
    print('It is a pangram.')