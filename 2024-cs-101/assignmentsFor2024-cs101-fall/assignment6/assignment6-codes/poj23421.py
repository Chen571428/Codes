#@Nickname: Chen571428
#@StuNum: 2400934013
import functools
weight, price, selected, ansRec, N, B = [], [], [], {}, 0, 0

def maxSure(x):
    if len(x):
        return max(x)
    else:
        return 0
@functools.lru_cache(maxsize=None,typed=False)
def biggestBaggedPrice(baggedVolume,baggedPrice,selection):
    global N, B, price, weight, selected, ansRec
    if ansRec.get(baggedVolume,0):
        return ansRec[baggedVolume]
    elif baggedVolume == 0:
        return baggedPrice
    else:
        selected.append(selection)
        ansRec[baggedVolume] = maxSure([biggestBaggedPrice(baggedVolume - weight[i],baggedPrice + price[i],i) for i in range(N) if baggedVolume - weight[i] >= 0 and i not in selected])
        selected.pop()
        return ansRec[baggedVolume]
        
def main():
    global N,B,price,weight
    N,B    = [int(x) for x in input().split()]
    price  = [int(x) for x in input().split()]
    weight = [int(x) for x in input().split()]
    print(biggestBaggedPrice(B,0,''))
    
if __name__=="__main__":
    main()