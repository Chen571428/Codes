#include<bits/stdc++.h>
using namespace std;
#define RI  int
typedef long long ll;
#define file(x) freopen(#x".in","r",stdin);\
                freopen(#x".out","w",stdout)
ll read()
{
    char ch=getchar();ll num=0;bool fg=0;
    while(ch<'0'||ch>'9') fg|=ch=='-',ch=getchar();
    while(ch>='0'&&ch<='9') num=num*10+ch-'0',ch=getchar();
    return fg?-num:num;
}
template<typename T=ll>
class node
{
    public:
        ll l,r;
        T dat,add;
        node():l(0),r(0),dat(0),add(0){}
        node(ll l,ll r,T dat,T add):l(l),r(r),dat(dat),add(add){/*printf("Node L:%lld R:%lld dat:%lld inited!\n",l,r,dat);*/}
};
template<typename T =ll>
class segTreeNode
{   
    private:
        node<T> * nd;
        segTreeNode * ls,* rs;
    public:
        segTreeNode const & pushup()
        {
            (nd->dat) = (ls->nd->dat) + (rs->nd->dat);
            return *this;
        }
        segTreeNode const & pushdown()
        {
            if((nd->add)==0) return *this;
            
            const ll mid = ((this->nd->l) + (this->nd->r))>>1;
            
            ls->nd->add += this->nd->add;
            ls->nd->dat += (this->nd->add) * (mid - (this->nd->l) + 1);
            
            rs->nd->add += this->nd->add;
            rs->nd->dat += (this->nd->add) * (this->nd->r - mid); 

            this->nd->add = 0;

            return *this;

        } 
        segTreeNode() {}
        segTreeNode(T info[],ll L,ll R)
        {
            if(L == R)
            {
                nd = new node<T>(L,R,info[L],0);
                ls = rs = nullptr;
            }
            else
            {
                ll mid = (L + R) >> 1;
                ls = new segTreeNode<T>(info,L,mid);
                rs = new segTreeNode<T>(info,mid+1,R);
                nd = new node<T>(L,R,0,0);
                this -> pushup();
            }
        }
        segTreeNode(ll L,ll R)
        {
            if(L == R)
            {
                nd = new node<T>(L,R,0,0);
                ls = rs = nullptr;
            }
            else
            {
                ll mid = (L + R) >> 1;
                ls = new segTreeNode<T>(L,mid);
                rs = new segTreeNode<T>(mid+1,R);
                nd = new node<T>(L,R,0,0);
                this -> pushup();
            }
        }
        segTreeNode const & update(T x,ll L,ll R)
        {
            if(L <= (nd -> l) && (nd -> r) <= R)
            {
                (this->nd->dat) += x * ((nd->r) - (nd->l) +1);
                (this->nd->add) += x;
                return *this;
            }
            ll mid = ((this->nd->l) +(this->nd->r))>>1;
            this -> pushdown();
            if(L <= mid) ls->update(x,L,R);
            if(mid+1 <= R) rs->update(x,L,R);
            return this -> pushup();
        }
        const T query(ll L, ll R)
        {
            if(L <= (nd -> l) && (nd -> r) <= R) return this->nd->dat;
            ll mid = ((nd -> l) + (nd -> r))>>1,res=0;
            this -> pushdown();
            if(L <= mid)res += ls->query(L,R);
            if(mid+1 <= R)res += rs->query(L,R);
            return res;
        }
};
template<typename T = ll>
class segTree
{
    private:
        segTreeNode<T> * mainNode;
    public:
        segTree(T info[],ll l,ll r) {mainNode = new segTreeNode<T>(info,l,r);}
        segTree(ll l,ll r) {mainNode = new segTreeNode<T>(l,r);}
        segTree const & update(T x,ll L,ll R){mainNode->update(x,L,R);return *this;} 
        const T query(ll L ,ll R){return mainNode->query(L,R);}
};
signed main()
{
    ll n = read(),m = read();
    ll * info = new ll[n+5];
    ll L,R,x;
    ll ans;
    for(RI i=1 ; i<=n ; i++)
        info[i]=read();
    segTree<ll> *SGT = new segTree<ll>(info,1,n);
    for(RI i=1 ; i<=m ; i++)
    {
        if(read()==1)
        {
            L = read(),R = read(),x = read();
            SGT -> update(x,L,R);
        }
        else
        {
            L = read(),R = read();
            printf("%lld\n",SGT -> query(L,R));
        }
    }
    return 0;
}