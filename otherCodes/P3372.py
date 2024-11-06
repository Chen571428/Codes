#@Nickname: Chen571428
#@StuNum: 2400934013
class node:
    def __init__(self,l,r,dat,add) -> None:
        self.l, self.r, self.dat, self.add ,self.mid = l, r, dat, add, (l+r) //2

class segTreeNode(node):
    def __pushup(self):
        self.dat = self.ls.dat + self.rs.dat

    def __pushdown(self):
        if self.add != 0:
            self.ls.add += self.add
            self.rs.add += self.add

            self.ls.dat += self.add * (self.mid - self.l + 1)
            self.rs.dat += self.add * (self.r - self.mid)

            self.add = 0

    def __init__(self,info,L,R) -> None:
        if L == R:
            node.__init__(self,L,R,info[L],0)
        else:
            mid = (L+R)//2
            self.ls = segTreeNode(info,L,mid)
            self.rs = segTreeNode(info,mid+1,R)
            node.__init__(self,L,R,0,0)
            self.__pushup()

    def update(self,L,R,x):
        if L <= self.l <= self.r <= R:
            self.dat += x * (self.r - self.l +1)
            self.add += x
        else:
            self.__pushdown()
            if L <= self.mid:
                self.ls.update(L,R,x)
            if self.mid+1 <= R:
                self.rs.update(L,R,x)
            self.__pushup()

    def query(self,L,R):
        if L <= self.l <= self.r <= R:
            return self.dat
        else:
            self.__pushdown()
            ans = 0
            if L <= self.mid:
                ans += self.ls.query(L,R)
            if self.mid+1 <= R:
                ans += self.rs.query(L,R)
            return ans

class segTree:
    def __init__(self,info,L,R) -> None:
        self.__mainNode = segTreeNode(info,L,R)

    def query(self,L,R):
        return self.__mainNode.query(L,R)
    
    def update(self,L,R,x):
        self.__mainNode.update(L,R,x)

def main():
    n, m=[int(x) for x in input().split()]
    info = [0]
    [info.append(int(x)) for x in input().split()]

    SGT = segTree(info,1,n)

    for i in range(m):
        operation = [int(x) for x in input().split()]
        if operation[0] == 1:
            SGT.update(operation[1],operation[2],operation[3])
        else:
            print(f"{SGT.query(operation[1],operation[2])}")

if __name__=="__main__":
    main()