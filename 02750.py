def ceil(x):
    if(x-int(x)!=0):
        return int(x)+1
    else:
        return int(x)
def main():
    rec=int(input())
    if(rec<=1 or rec % 2 != 0):
        print('0 0')
    else:
        print('{} {}'.format(ceil((rec/4)),ceil((rec/2))))
main()