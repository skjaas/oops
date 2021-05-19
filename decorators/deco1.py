def admin_required(func):
    def wrapper(user,pin):
        if user != "admin":
            raise Exception("you are noy allowed")
        else:
            return func(user,pin)
    return wrapper


@admin_required
def change_pin(user, pin):
    mypin = pin
    return mypin
@admin_required
def delete_account(user,acno):
    return str(acno)+"deleted"
try:
    print(change_pin("Arya",689108))
    print(delete_account("arya",346574589))
except Exception as e:
    print(e.args)
print(delete_account("admin",346574589))