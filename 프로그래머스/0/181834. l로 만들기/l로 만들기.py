def solution(myString):
    return ''.join('l' if x < 'l'  else x for x in myString)