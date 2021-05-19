
def push():
    global top,size
    if(top<size):
        element=int(input(":"))
        lst.append(element)
        top+=1
        print(lst)
    else:
        print("List Full",lst)

def pop():
    global top
    if(top<=0):
        print("List empty",lst)
    else:
        lst.pop()
        top-=1
        print(lst)
lst=[]
top=0
size=int(input("Enter the size of the stack:"))
choice=True
while(choice):
    option=int(input("1.Push 2.Pop\n :"))
    if(option==1):
        push()
    elif(option==2):
        pop()
    else:
        choice=False
