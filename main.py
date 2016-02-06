from determinist import *

print("coucou")

test = WeakSchur([[1],[2,3,6]])
test.display()
test.save("yop")
test.vals=[[]]
test.display()
print("load")
test.load("yop")
test.display()
test.verify()

