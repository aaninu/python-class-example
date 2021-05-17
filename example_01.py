

class test:
    def __init__(self):
        print("ana are mere")

    def t(self, x):
        print ("text: " + str(x))

class wow(test):
    def __init__(self):
        super(wow, self).__init__()

    def t(self, x):
        print ("wow class here")
        super(wow, self).t(x)
    

y = test()
y.t("aaa")

z = wow()
z.t("soricei")
