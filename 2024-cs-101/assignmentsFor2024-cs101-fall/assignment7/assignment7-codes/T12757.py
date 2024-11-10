#@Nickname: Chen571428
#@StuNum: 2400934013
unitNum = 'thousand million'
singleNum = 'zero  one  two  three  four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen  seventeen  eighteen  nineteen  twenty  thirty  forty  fifty  sixty  seventy  eighty  ninety'
numOfStr  = {
        'zero':0, 'one' :1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
        'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,
        'nineteen':19,'twenty':20,'thirty':30,'forty':40,'fifty':50,'sixty':60,'seventy':70,'eighty':80,'ninety':90,
        'hundred':100,'thousand':1000,'million':1000000
    }
def main():
    ans ,flag ,currentSingleNum= 0 , 1 , 0 
    numStr = input().split()
    if numStr[0] == 'negative':
        flag = -1
        del numStr[0]
    while len(numStr) >0:
        while len(numStr) > 0 and numStr[0] in singleNum:
            currentSingleNum += numOfStr[numStr[0]]
            del numStr[0]
        if len(numStr) == 0:
            ans += currentSingleNum
            break
        elif numStr[0] == 'hundred':
            currentSingleNum = currentSingleNum * numOfStr[numStr[0]]
            del numStr[0]
            if len(numStr) == 0:
                ans += currentSingleNum
                break
        else:
            ans += currentSingleNum * numOfStr[numStr[0]]
            del numStr[0]
            currentSingleNum = 0
    
    print(ans*flag)

if __name__=="__main__":
    main()