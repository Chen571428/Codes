#@Nickname: Chen571428
#@StuNum: 2400934013
import heapq
def main():
    N,D = [int(x) for x in input().split()]
    heights = [int(input()) for _ in range(N)]
    used = {}
    curMax,pos = 0,0
    curMin,curVal = 0x3f3f3f3f,0
    n=N
    curQue = []
    while n > 0:
        pos ,curMax ,curMin = 0 ,-0x3f3f3f3f ,0x3f3f3f3f
        curVal = [0x3f3f3f3f,0]

        while pos < N:
            if not used.get(pos):
                if curMax == -0x3f3f3f3f or curMin == 0x3f3f3f3f:
                    curMin = curMax = heights[pos]
                curMax = max(curMax,heights[pos])
                curMin = min(curMin,heights[pos])
                if curMax - heights[pos] <= D and heights[pos] - curMin <= D:
                    heapq.heappush(curQue,heights[pos])
                    used[pos] =1; n-=1
            pos += 1
        
        while len(curQue) > 0:
            print(heapq.heappop(curQue))
    
    
if __name__=="__main__":
    main()
# O(不会算) 总之最慢时退化为N^2

#@Nickname: Chen571428
#@StuNum: 2400934013

# # 思路：在值域上维护 到当前位置之前的所有节点对应高度 的区间层数最大值
# #      即维护前缀区间层数最值
# #      当前位置节点所属层数等于 值域上[0,Hi-Di) and (Hi+Di,MAXH]部分 的层数最大值 +1
# #      
# #      再将当前位置节点对应层数更新到前缀节点所维护的区间上
# # 
# # 不知道哪里写错了，总之写错了
# # SegTree From P3372.py
# class node:
#     def __init__(self,l,r,dat) -> None:
#         self.l, self.r, self.dat ,self.mid = l, r, dat, (l+r) //2

# class segTreeNode(node):
#     def __pushup(self):
#         ans = self.dat
#         if self.ls.initialized:
#             ans = max(ans,self.ls.dat)
#         if self.rs.initialized:
#             ans = max(ans,self.rs.dat)
#         self.dat = ans
#         # print(f"{self.l} {self.r} pushed up to {self.dat} ")

#     # def __pushdown(self):
#     #     if self.add != 0:
#     #         self.ls.add += self.add
#     #         self.rs.add += self.add

#     #         self.ls.dat += self.add * (self.mid - self.l + 1)
#     #         self.rs.dat += self.add * (self.r - self.mid)

#     #         self.add = 0

#     def __init__(self,flag,L,R) -> None:
#         self.initialized = flag
#         if self.initialized:
#             node.__init__(self,L,R,0)
#             self.ls = segTreeNode(0,L,R)
#             self.rs = segTreeNode(0,L,R)
    
#     def update(self,L,R,x):
#         # print(f"func upd at {L} {R} {self.l} {self.r} {x} has loaded!")
#         if L <= self.l <= self.r <= R:
#             self.dat = max(self.dat,x)
#             # print(f"Node {self.l},{self.r} has upd to {self.dat}!")
#         else:
#             if L <= self.mid:
#                 if not self.ls.initialized:
#                     self.ls.__init__(1,self.l,self.mid)
#                 self.ls.update(L,R,x)
#             if self.mid+1 <= R:
#                 if not self.rs.initialized:
#                     self.rs.__init__(1,self.mid+1,self.r)
#                 self.rs.update(L,R,x)
#             self.__pushup()

#     def query(self,L,R):
#         if L > R:
#             return 0
#         if L <= self.l <= self.r <= R:
#             return self.dat
#         else:
#             ans = 0
#             if L <= self.mid:
#                 if self.ls.initialized:
#                     ans = max(ans,self.ls.query(L,R))
#             if self.mid+1 <= R:
#                 if self.rs.initialized:
#                     ans = max(ans,self.rs.query(L,R))
#             return ans

# class segTree:
#     def __init__(self,L,R) -> None:
#         self.__mainNode = segTreeNode(1,L,R)

#     def query(self,L,R):
#         return self.__mainNode.query(L,R)
    
#     def update(self,L,R,x):
#         self.__mainNode.update(L,R,x)


# def main():
#     N,d = [int(x) for x in input().split()]
#     heights = [int(input()) for _ in range(N)]
#     maxHeight = max(heights) + 3
    
#     SGT = segTree(1,maxHeight)
#     layers = [[]]
#     maxLayerNum = -1
#     pos = 0
#     while pos < N:
#         curLayerNum = max(SGT.query(1,heights[pos] - d - 1 ) , SGT.query(heights[pos] + d + 1, maxHeight)) + 1
#         if curLayerNum > maxLayerNum:
#             layers.append([])
#             maxLayerNum = curLayerNum
#         layers[curLayerNum].append(heights[pos])
#         SGT.update(heights[pos],heights[pos],curLayerNum)
#         pos += 1

#     for layer in layers:
#         [print(x) for x in sorted(layer)]

# if __name__=="__main__":
#     main()