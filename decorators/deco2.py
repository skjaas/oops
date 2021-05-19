


def vaccination_portal(funct):
    def wrapper(**kwargs):
        age = kwargs["age"]
        health_issue = kwargs["health_issue"]
        if (age < 65) or (health_issue == False):
            raise Exception("You are not allowed")
        else:
            return funct(**kwargs)

    return wrapper


@vaccination_portal
def vaccination_portal(**kwargs):
    return "you are allowed for vaccination"
try:
    print(vaccination_portal(name="ram",age=65,address="address",health_issue=True))
except Exception as e:
    print(e.args)

# age = above>65
# or health_issues = True