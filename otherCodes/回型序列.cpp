#include <stdio.h>
#include <math.h>
#include <stdbool.h> // 引入bool类型
/* C语言初始模板程序 */

int main(void) { 
	//printf("Hello world!");
	int row;
	int col;
	scanf("%d%d",&row,&col);
	double o=row;
	int a[105][105];
	for (int y=0;y<row;y++){
	    for (int z=0;z<col;z++){
	        scanf("%d",&a[y][z]);
	    }
	}
    int current_direction = 0; // 第一行默认向右
    
    int current_x = 0,current_y = 0;// 当前坐标。起始点是（0，0）
    bool printed[105][105]; // 一般多开一点防止出事
    for(int i = 0;i < row;i++)
        for(int j = 0;j < col;j++)
            printed[i][j] = 0; //初始化为都没有输出过
    const int right = 0,down = 1,left = 2,up = 3;
    // 用0 表示现在在向右输出
    //  1             下
    //  2             左
    //  3             上
    //可以用enum实现，更加方便（如果学了enum的话
    const int next[4][2] = {{0,1},{1,0},{0,-1},{-1,0}};
    int nexti,nextj;
    for(int i = 1;i<=(row * col);i++)
    {
        printf("%d\n",a[current_x][current_y]);
        printed[current_x][current_y] = 1;

        nexti = current_x + next[current_direction][0];
        nextj = current_y + next[current_direction][1]; // 产生下一个坐标

        if(nexti < 0 ||nexti >= row||nextj < 0||nextj >= col||printed[nexti][nextj]) // 如果下一个坐标超出界限了或者已经输出过了
            current_direction = (current_direction+1) %4; // 转弯。%表示取除法的余数。可以自己模拟一下看看是不是对的

        current_x = current_x + next[current_direction][0]; // 产生真正的下一个坐标。如果转弯了，就与nexti nextj不同。否则与其相同
        current_y = current_y + next[current_direction][1];
    }
    return 0;
}
/*
5 4
1  2  3  4  
14 15 16 5
13 20 17 6
12 19 18 7 
11 10 9  8 
*/