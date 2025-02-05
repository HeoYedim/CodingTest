def solution(num_list):
    # next()는 이터레이터의 다음 요소 가져오는 함수
    # 요소가 없을 경우 오류가 생기니 기본값 반환할 수 있도록 하기
    # next(이터레이터 변수 명, deault 값)
    return next((i for i, num in enumerate(num_list) if num < 0), -1)