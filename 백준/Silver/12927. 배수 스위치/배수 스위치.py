light = ['N'] + list(input())
switch = 0

for i in range(1, len(light)):
    if light[i] == 'Y':
        for j in range(i, len(light), i):
            if light[j] == 'Y':
                light[j] = 'N'
            else:
                light[j] = 'Y'
        switch += 1
        
print(switch)