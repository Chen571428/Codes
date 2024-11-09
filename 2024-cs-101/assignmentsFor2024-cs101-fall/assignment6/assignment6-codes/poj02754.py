#@Nickname: Chen571428
#@StuNum: 2400934013
import functools
ans = []
def search_answer(n,procQueenLine,ansRec,occuMarker1,occuMarker2):
    global ans
    if(procQueenLine == n+1):
        ans.append(int(ansRec))
        return
    else:
        if(len(ansRec)):
            x ,y = procQueenLine-1, int(ansRec[len(ansRec)-1])
            # [occuMarker.append((x+_,y))   for _ in range(1,n+1)]
            # [occuMarker.append((x+_,y+_)) for _ in range(1,n+1)]
            # [occuMarker.append((x+_,y-_)) for _ in range(1,n+1)]
            occuMarker1.append(x+y)
            occuMarker2.append(x-y)

        [search_answer(n,procQueenLine+1,ansRec+'{}'.format(_),occuMarker1,occuMarker2) for _ in range(1,9) \
         if (str(_) not in ansRec) and (procQueenLine + _ not in occuMarker1) and (procQueenLine - _ not in occuMarker2)]
        
        if(len(ansRec)):
            del occuMarker1[-1],occuMarker2[-1]
def main():
    global ans
    n = int(input())
    search_answer(8,1,'',[],[])
    ans.sort()
    [print(ans[int(input())-1]) for x in range(n)]
if __name__=="__main__":
    main()