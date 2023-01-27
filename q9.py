class validity:

    def f(str):

        a= ['()', '{}', '[]'] 

        for i in a:
            for j in a:

                str = str.replace(j, '') 

        return not str 

s = input("enter : ")

print(s, "-", "is balanced" 

      if validity.f(s) else "is Unbalanced")