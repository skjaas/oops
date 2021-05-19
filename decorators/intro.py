# decorator function uses when we want to add new features to the
# existing function without chnaging that function

def revert_values(func):
    def wrapper(no1, no2):
        if no1 < no2:
            (no1, no2) = (no2, no1)
        return func(no1, no2)
    return wrapper

@revert_values
def div(num1, num2):
    return num1/num2

@revert_values
def sub(no1, no2):
    return no1-no2

print(div(2, 10))
print(sub(8, 10))
