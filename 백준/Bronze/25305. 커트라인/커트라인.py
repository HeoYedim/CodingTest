student, winner = input().split()
score = list(map(int, input().split()))

score.sort(reverse=True)
print(score[int(winner)-1])