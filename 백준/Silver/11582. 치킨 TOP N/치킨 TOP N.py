N=int(input().strip())
chicken_score=list(map(int,input().strip().split()))
k=int(input().strip())

tmp=[]

for i in range(0,N,N//k):
    tmp+=sorted(chicken_score[i:i+N//k])
print(" ".join(str(i) for i in tmp))