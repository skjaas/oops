class Pycharm:
    def compile(self):
        print("Compile")

    def execute(self):
        print("exeute")


class Vscode:
    def compile(self):
        print("Compile")

    def execute(self):
        print("exeute")



class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()

p = Programmer()
pyc = Pycharm
p.coding(pyc)