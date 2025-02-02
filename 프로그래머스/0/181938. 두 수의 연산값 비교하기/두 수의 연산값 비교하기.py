def solution(a, b):
    # f"{a}{b}" : 숫자를 문자열로 변환하는 문자열 포맷팅
    return max(int(f"{a}{b}"), 2 * a * b)