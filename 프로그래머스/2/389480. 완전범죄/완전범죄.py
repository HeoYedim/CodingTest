def solution(info, n, m):
    cur_states = set()
    cur_states.add((0, 0))  # 시작 상태: A와 B의 흔적이 각각 0

    # 0 [1, 2], 1 [2, 3] ...
    for i, (a_trace, b_trace) in enumerate(info):
        next_states = set()
        for a_sum, b_sum in cur_states:
            # A가 이번 물건을 훔치는 경우
            new_a = a_sum + a_trace
            if new_a < n:
                next_states.add((new_a, b_sum))
            # B가 훔치는 경우
            new_b = b_sum + b_trace
            if new_b < m:
                next_states.add((a_sum, new_b))
        cur_states = next_states  # 다음 반복을 위해 업데이트

    if not cur_states:
        return -1

    return min(a for a, b in cur_states)