
print ("哈哈啊")

tunle = {1,"a"}

print(tunle)

def foo():
    print("foo() function calling .....")

    def bar():
        print("bar() function calling ....")

foo()  # 不会调用 bar()
