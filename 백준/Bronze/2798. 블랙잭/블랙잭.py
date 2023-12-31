from itertools import combinations

N, M = map(int, input().split())
card_list = map(int, input().split())
answer = 0

for cards in combinations(card_list, 3):
    cards_sum = sum(cards)
    if answer < cards_sum and cards_sum <= M:
        answer = cards_sum
print(answer)