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
char str_a[502],str_b[502];
double ratios = 0.0d;
double same_count = 0.0d;
signed main()
{
    scanf("%lf\n%s\n%s",&ratios,str_a,str_b);
    int len_a = strlen(str_a),len_b = strlen(str_b);
    if(len_a != len_b)
        printf("error\n");
    else
    {
        for(int i=0;i<len_a;i++) // scanf的输入中没有\0
        {
            if((str_a[i] == 'A' || str_a[i] == 'G'|| str_a[i] == 'C'|| str_a[i] == 'T') && (str_b[i] == 'A' || str_b[i] == 'G'|| str_b[i] == 'C'|| str_b[i] == 'T'))
            {// 你这里的判断好像也写错了。每个都是才行，而不是每个都不是才不行
                if(str_a[i] == str_b[i])
                    same_count += 1.0d; //d后缀表面这是一个双精度浮点数
            }
            else
            {
                printf("error\n");
                return 0;
            }
        }
        if((same_count / (double)len_a) >= ratios) // 都是浮点数可以直接比较
            printf("yes\n");
        else
            printf("no\n");
    }
    return 0;
}