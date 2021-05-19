def enque():
    global size
    if(len(lst)<size):
        element=int(input(":"))
        lst.append(element)
        for i in lst:
            print(i)
    else:
        print("Queue Full")
        for i in lst:
            print(i)


def deque():
    if(len(lst)==0):
        print("Queue Empty")
    else:
       lst.pop(0)
       for i in lst:
           print(i)

lst=[]
top=0
end=0
size=int(input("Enter the size:"))
choice=True
while(choice):
    option=int(input(".............................1.Insert 2.Delete...................................\n:"))
    if(option==1):
        enque()
    elif(option==2):
        deque()
    else:
        choice=False