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
        case "**":
            return a ** b
precedence = {"+":1,"-":1,"*":2,"/":2,'**':3,"(":0}
def prase_input(arr):
    arr = arr.split()
    arr.append(")")
    print(arr)
    no_arr = []
    symbols = []
    symbols.append("(")
    for i in arr:
        match(i):
            case "(":
                symbols.append("(")
            case "+" | "-" | "/" | '*' | '**':
                current_precedence = precedence[i]
                past_precedence = precedence[symbols[-1]]
                if(past_precedence >= current_precedence):
                    b = no_arr.pop()
                    a = no_arr.pop()
                    c = symbols.pop()
                    no_arr.append(evaluate(a,b,c))
                symbols.append(i)
            case ")":
                ok = symbols.pop()
                while(ok != '('):
                  b = no_arr.pop()
                  a = no_arr.pop()
                  c = evaluate(a,b,ok)
                  print(b,a,ok,c)
                  no_arr.append(c)
                  print(no_arr)
                  ok = symbols.pop()
            case _:
                no_arr.append(int(i))
    return no_arr[0]

no_arr = prase_input(input("Please enter each character seperated by sapces "
                           ))
print(no_arr)

