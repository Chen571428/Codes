#include<bits/stdc++.h>
using namespace std;
#define RI int
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
signed main()
{
    ll a=read();
    if(a<=1||a%2!=0) {printf("0 0\n"); return 0;}
    printf("%d %d\n",(int)ceil(a/4.0),(int)ceil(a/2.0));
    return 0;
}