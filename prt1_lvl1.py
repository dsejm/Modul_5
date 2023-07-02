class StringVar:
    def __init__(self, str="None"):
        self.str = str

    def get(self):
       print(self.str)

    def set(self, str):
        self.str = input("Переназначте текст строки ")
        return self.str

some_string = StringVar(str="Hello")
some_string.get()
some_string.set("")
some_string.get()
one_more_string = StringVar()
one_more_string.get()
one_more_string.set("")
one_more_string.get()
one_more_string.get()
one_more_string.get()
one_more_string.get()
print(one_more_string.__dict__)


