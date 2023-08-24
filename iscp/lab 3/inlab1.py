letters = input().split()
find = input()
for i in letters:
    if(i > find):
        print(i)
        break