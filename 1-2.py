def solution(array, commands):
    answer = []
    for a in commands :
        b= sorted(array[a[0]-1:a[1]])
        answer.append(b[a[2]-1])
    return answer