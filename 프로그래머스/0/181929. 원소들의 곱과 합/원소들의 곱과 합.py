from math import prod

def solution(num_list):
    # prod : 리스트 모든 요소를 한 줄로 곱
    return int(sum(num_list) ** 2 > prod(num_list))