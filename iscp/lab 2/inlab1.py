def evaluate(a,b,char):
    match char:
        case '+' :
            return a + b
        case '-' :
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b

def prase_input(arr):
    no_arr = []
    for i in arr:
        match(i):
            case "+" | "-" | "/" | '*' :
                a = no_arr.pop()
                b = no_arr.pop()
                no_arr.append(evaluate(b,a,i))
            case _:
                no_arr.append(int(i))
    return no_arr

no_arr = prase_input(["4","13","5","/","+"])
print(no_arr)

