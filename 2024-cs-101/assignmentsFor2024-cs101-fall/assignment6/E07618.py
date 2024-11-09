#@Nickname: Chen571428
#@StuNum: 2400934013

import functools
def cmp(a,b):
    if a[0]>b[0]:
        return -1
    elif a[0]==b[0]:
        return a[2]<b[2]
    else:
        return 1
def main():
    info ,pq ,cnt,I,age,inputPatient= [], [],0,1,0,[]
    N= int(input())
    while I <= N:
        inputPatient = input().split()
        age = int(inputPatient[1])
        if age >= 60:
            pq.append((age,inputPatient[0],I))
        else:
            info.append(inputPatient[0])
        I += 1
    pq.sort(key=functools.cmp_to_key(cmp))
    [print(i[1]) for i in pq]
    [print(i) for i in info]
if __name__=="__main__":
    main()