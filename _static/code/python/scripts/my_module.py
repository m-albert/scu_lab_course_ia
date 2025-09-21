# my_module.py
s = "This is a string from my_module."
a = [0, 1, 2, 3]

def my_fun(arg):
    print(arg)

class My_Class:
    def __init__(self, id=1):
        self.id = id
        print(self.id)

if __name__ == "__main__":
    print("Let's test our code:")
    m = My_Class(id=42)
    assert(m.id == 42)

