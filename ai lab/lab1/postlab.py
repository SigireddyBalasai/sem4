class Jug:
    capicity : int
    current_filled : int
    target : int = None
    def __init__(self,capacity):
        self.capacity = capacity
        self.current_filled = 0
    def transfer_to(self,jug2:'Jug'):
        if(jug2.capacity - jug2.current_filled < self.current_filled):
            change = jug2.capacity - jug2.current_filled + self.current_filled
            self.current_filled -= jug2.capacity - jug2.current_filled
            jug2.current_filled = jug2.capacity

        else:
            jug2.current_filled += self.current_filled
            self.current_filled = 0
    def fill_full(self):
        self.current_filled = self.capacity
    def empty(self):
        self.current_filled = 0
    def target_attained(self):
        if(self.target_attained == 0):
            return True
        elif(self.target_attained != 0):
            return self.current_filled == self.target
        return True
    def __str__(self):
        return f"Capacity : {self.capacity} , target : {self.target} , current_filled : {self.current_filled}"


jug1 = Jug(int(input("Please enter the size of jug 1")))
jug2 = Jug(int(input("Please enter the size of jug 2")))

target1 = input("Please enter target of jug 1")
target2 = input("Please enter target of jug 2")
if(target1 != ""):
    target1 = int(target1)
else:
    target1 = 0
if(target2 != ""):
    target2 = int(target2)
else:
    target2 = 0

jug1.target = target1
jug2.target = target2
no_steps = 0
total_water = int(input("please enter total amount of water available"))
jug_f = Jug(total_water)
jug_f.fill_full()
while((not jug1.target_attained()) or (not jug2.target_attained())):
    print("*"*50)
    print("Please enter 1 to fill full for 1")
    print("Please enter 2 to fill full for 2")
    print("Please enter 3 to transfer from 1 to 2")
    print("Please enter 4 to transfer from 2 to 1")
    print("Please enter 5 to empty 1")
    print("Please enter 6 to empty 2")
    command = int(input())
    match(command):
        case 1:
            jug_f.transfer_to(jug1)
        case 2:
            jug_f.transfer_to(jug2)
        case 3:
            jug1.transfer_to(jug2)
        case 4:
            jug2.transfer_to(jug1)
        case 5:
            jug1.empty()
        case 6:
            jug2.empty()
    no_steps += 1
    print(jug1)
    print(jug2)
print("The programm is completed in ",no_steps)

