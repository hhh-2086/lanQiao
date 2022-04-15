#include<bits/stdc++.h>
using namespace std;
long long ans=0;
 int ss[3][4]={0,0,0,0,0,0,0,0,0,0,0,0};
 
 void dfs(int x,int y){
 	if(x>2||x<0||y>3||y<0) return ;   
 	  //运行到这里，说明已经越界了，则需要返回上一级的dfs()，然后换个方向继续寻找   
 	if(ss[x][y]==0) return ;       
 	 //这里，就是这个点不是需要剪的位置，则返回上一级的dfs()函数，
 	 //继续执行未完成的dfs()函数，也就是换个方向继续找 
 	ss[x][y]=0;    //找到了，则将这个点标记 
 	dfs(x+1,y);
 	dfs(x,y+1);
 	dfs(x-1,y);
 	dfs(x,y-1);
 	/*
 	例如：
 	 通过cc(1,1)函数传来起始点，然后将这点标记，然后进入下一级的dfs(2,1)函数，
 	如果 ss[2][1]==0 则返回上一级dfs()函数，也就是dfs(1,1),继续执行未完成的语句，
	也就是(1,2),如果也没有，就又返回dfs(1,1)，继续执行(0,1),如果没有，则返回dfs(1,1)，
	 继续执行dfs(1,0)，如果还是没有，则dfs(1,1)已经执行完成了
	那么接下来dfs(1,1)要返回了，便回到cc()函数，
	继续执行未完成的语句，也就是 int flag=0的位置，直到cc()函数结束  	
 	*/
 }

//判断某5个数是否可行
bool cc(int a[12]){
	int k=0; 
	int x,y;//起点 
	for(int i=0;i<3;i++){
		for(int j=0;j<4;j++){
			if(a[k]==1){
				x=i;y=j;    //起点，就是从这个点，开始往四周寻找 
			}
			ss[i][j]=a[k++];
		}
	}
	dfs(x,y);    //开始寻找 
	int flag=0;
	
	for(int i=0;i<3;i++){
		for(int j=0;j<4;j++){
			if(ss[i][j]==1) flag=1;
			//5个邮票中存在没有遍历到的，也就是存在一个数，周围没有连着 
		}
	}
	if(flag==1) return false;  
	return true;
}
int main(){
	int a[12]={0,0,0,0,0,0,0,1,1,1,1,1};
	do{
		if(cc(a)) ans++;
	}while(next_permutation(a,a+12));       //对a数组进行全排列，没有重复的 
		//  next_permutatio n每执行一次，都要调用 cc()函数 ，形成一种全排列 
	
	cout<<ans;
	return 0;
} 



