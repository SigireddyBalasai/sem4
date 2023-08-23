boat_position = 0
cannibals_left = 3
missionaries_left = 3
cannibals_right = 0
cannibals_right = 0
initial_state = [[3,3],[0,0]]
goal_state = [[0,0],[3,3]]
state = initial_state
while(state != goal_state):
    print("Please enter 1 to move two cannabals")
    print("Please enter 2 to move one cannabals")
    print("Please enter 3 to move one cannabals and one missionary")
    print("Please enter 4 to move one missionary")
    print("Please enter 5 to move two missionaries")
    if((state[0][1] > state[0][0]) and (state[1][1] > state[1][0])):
                print("Sorry you killed missionaries")
                break;
    change = int(input())
    match change:
        case 1:
            if(boat_position == 0):
                if(state[0][1] > 1):
                    state[1][1] += 2
                    state[0][1] -= 2
                else:
                    print("Sorry the solution is not approved")
            else:
                if(state[1][1] > 1):
                    state[1][1] -= 2
                    state[0][1] += 2
                else:
                    print("Sorry the solution is not approved")
        case 2:
            if(boat_position == 0):
                if(state[0][1] > 0):
                    state[1][1] += 1
                    state[0][1] -= 1
                else:
                    print("Sorry the solution is not approved")
            else:
                if(state[1][1] > 0):
                    state[1][1] -= 1
                    state[0][1] += 1
                else:
                    print("Sorry the solution is not approved")
        case 3:
            if(boat_position == 0):
                if(state[0][1] > 1 and state[0][0] > 1):
                    state[1][1] += 1
                    state[0][1] -= 1
                    state[0][0] -= 1
                    state[1][0] += 1
                else:
                    print("Sorry the solution is not approved")
            else:
                if(state[1][0] > 1 and state[1][1] > 1):
                    state[1][1] -= 1
                    state[0][1] += 1
                    state[0][0] += 1
                    state[1][0] -= 1
                else:
                    print("Sorry the solution is not approved")
        case 4:
            if(boat_position == 0):
                if(state[0][0] > 0):
                    state[1][0] += 1
                    state[0][0] -= 1
                else:
                    print("Sorry the solution is not approved")
            else:
                if(state[1][0] > 0):
                    state[1][0] -= 1
                    state[0][0] += 1
                else:
                    print("Sorry the solution is not approved")
        case 5:
            if(boat_position == 0):
                if(state[0][0] > 1):
                    state[1][0] += 2
                    state[0][0] -= 2
                else:
                    print("Sorry the solution is not approved")
            else:
                if(state[1][0] > 1):
                    state[1][0] -= 2
                    state[0][0] += 2
                else:
                    print("Sorry the solution is not approved")
    print("positions are ",state)
    boat_position = (boat_position + 1) % 2
        
        


            
        
