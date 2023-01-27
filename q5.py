def hyphen(string):
    string1 = string.split("-")
    list1 = []

    for i in range(len(string1)) :
        b = string1[i]
        list1.append(b)
    list1.sort()
    c = str("-".join(list1))
    return c

string = str(input('Enter a string :'))
a = hyphen(string)
print(a)