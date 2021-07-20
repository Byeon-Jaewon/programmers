def solution(s, n):
    answer = ''
    for i in s :
        I = ord(i)
        if (64 < I and I < 91):
            I += n
            if (I > 90):
                I-=26
        if (96 < I and I < 123):
            I+=n
            if (I > 122) :
                I-=26
        answer += chr(I)
    return answer