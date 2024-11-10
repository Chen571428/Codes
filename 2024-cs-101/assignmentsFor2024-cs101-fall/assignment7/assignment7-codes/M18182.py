#@Nickname: Chen571428
#@StuNum: 2400934013
from queue import PriorityQueue as pq
def main():
    nCases, caseNum= int(input()) , 1
    while caseNum <= nCases:
        n, m, b = [int(x) for x in input().split()]
        tkNum ,tks,tking,flag,tkset= 1,{0:pq()},[],False,{0:0}
        while tkNum <= n:
            tick, damage= [int(x) for x in input().split()]
            if not tkset.get(tick):
                tkset[tick] = 1
                tking.append(tick)
            if not tks.get(tick):
                tks[tick] = pq()
            tks[tick].put(-damage)
            tkNum +=1
        tking.sort()
        for tick in tking:
            for i in range(min(tks[tick].qsize(),m)):
                b += tks[tick].get()
                if b <= 0:
                    print(tick)
                    flag = True
                    break
            if flag:
                break
        if not flag:
            print("alive")
        caseNum += 1


if __name__=="__main__":
    main()