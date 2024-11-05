def main():
    year=int(input())
    print('NY'[int(year%4==0 and ((year%100!=0) or year % 400 == 0))])
if __name__=='__main__':
    main()