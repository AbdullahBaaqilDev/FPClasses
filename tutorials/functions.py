# functions syntex
def print_names():
    print("abdullah")
    print("mohammed")
    print("ali")
    print("hamzah")
    print("hamzah x 2")

print_names()
print_names()

# functions parameters
def make_math(first_num,opreration,second_num):
    match opreration:
        case "+":
            print(first_num + second_num)
        case "-":
            print(first_num - second_num)
        case "x" | "*":
            print(first_num * second_num)
        case "/":
            print(first_num / second_num)
            
make_math(131,"*",621)

# pass a tuple to the parameter & return
def get_SMA(*numbers):
    full_number = sum(numbers)
    full_number /= len(numbers)
    
    return full_number

SMA = get_SMA(1,5,71,13,57,1)
print(SMA)

# pass dictionary to the parameter & pass
def student(**info):
    print(info)
    print(info.get("last_name","unknown") + " is your last name")

student(first_name = "abdullah",last_name = "baaqeil")

def empty_func():
    pass # means nothing

empty_func()