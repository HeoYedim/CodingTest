zoac_data = list(input())

start = 'A'
time = 0

for i in zoac_data:
    left = ord(i) - ord(start)
    right = ord(start) - ord(i)
    
    time += min(left%26, right%26)
    start = i
    
print(time)