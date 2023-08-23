temperatures = list(map(int,input().split()))
ok = len(temperatures)
answers = [0]*ok
for i in range(ok):
    current = temperatures[i]
    for j in range(i+1,ok):
        if(temperatures[j] - current > 0):
            print(j-i)
            answers[i] = j - i
            break;
print(answers)
