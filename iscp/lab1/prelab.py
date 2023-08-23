class Stack(list):
    def __init__(self):
        self.stack = []
    def push(self,data : int) -> None:
        self.stack.append(data)
    def pop(self):
        try:
            return self.stack.pop()
        except:
            return None
def find_largest_in_stack(stack : Stack):
    max_element = 0
    ok = stack.pop()
    while(ok is not None):
        if(ok >  max_element):
            max_element = ok
        ok = stack.pop()
    return max_element
def main():
    no_of_commands = input("Please enter the number of elements")
    command_list = input("Please enter the elements seperated by ' '")
    commands = [i for i in command_list.split()]
    stack = Stack()
    for command in commands:
        if(command[0] == "1"):
            stack.push(int(command[1]))
            print("Added element ",command[1])
        elif(command[0] == "2"):
            print("Popper ",stack.pop())
        elif(command[0] == "3"):
            print("the largest element is ",find_largest_in_stack(stack))
main()

