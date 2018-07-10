///A* search 
///MD Abdullah Al Nasim
#include <bits/stdc++.h>
using namespace std;
#define r 4
string dest_1d = "123456789ABCDEF#";
string dest_2d[r] = {"1234", "5678", "9ABC", "DEF#"};
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
class node{
    public:
    string s1d;
    string s2d[r];
    node(){
    }
    node(string s){
        s1d = s;
        for(int i = 0; i <r; i++){
            string s1 = "";
            for(int j = 0; j < r ;j++) s1 += s[i*r+j];
            s2d[i] = s1;
        }
    }
    void print(){
        for(int i = 0; i <r; i++) cout<<s2d[i]<<endl;
        cout<<endl;
    }
    friend bool operator < (const node& lhs, const node& rhs);
    friend bool operator > (const node& lhs, const node& rhs);
};
map<string, bool>visited;
map<string, int>dis;
map<string, string>parent;
node fn = node(dest_1d);

int h1(node s1){
    string s = s1.s1d;
    int sum = 0;
    for(int i = 0; i <s.length(); i++) sum += (s[i]!=dest_1d[i]);
    //cout<<sum<<endl;
    return sum;
}

bool operator < (const node& lhs, const node& rhs){
    return dis[lhs.s1d]+h1(lhs) < dis[rhs.s1d]+h1(rhs);
}
bool operator > (const node& lhs, const node& rhs)
{
    return dis[lhs.s1d]+h1(lhs) > dis[rhs.s1d]+h1(rhs);
}

bool valid(int x, int y){
    if(x<0||y<0||x>=r||y>=r) return false;
    return true;
}

void bfs(node source){
    priority_queue<node,vector<node>, greater<vector<node>::value_type> > pq;
	pq.push(source);
	visited[source.s1d]= true;
	dis[source.s1d] = 0;
	parent[source.s1d] = source.s1d;
	while(!pq.empty()){
		node from = pq.top();
		//cout<<"f(n) value = "<<dis[from.s1d]+h1(from)<<endl;
		visited[from.s1d] = true;
		pq.pop();
		int blank_x = -1, blank_y = -1;
		for(int i = 0; i <r; i++){
            for(int j = 0; j <r; j++){
                if(from.s2d[i][j] == '#'){
                    blank_x = i;
                    blank_y = j;
                }
            }
		}
		for(int i = 0; i <r; i++){
            string nn[r];
            if(valid(blank_x+dx[i], blank_y+dy[i])){
                for(int j = 0; j <r; j++){
                    nn[j] = from.s2d[j];
                }
                swap(nn[blank_x+dx[i]][blank_y+dy[i]], nn[blank_x][blank_y]);
                string n = "";
                for(int j = 0; j <r; j++){
                    n += nn[j];
                }
                node to = node(n);
                if(visited[to.s1d]) continue;
                visited[to.s1d] = true;
                pq.push(to);
                parent[to.s1d]=from.s1d;
                dis[to.s1d] = dis[from.s1d] + 1;
                //to.print();
                //cout<<dis[to.s1d]<<endl;
                if(to.s1d == dest_1d) return;
                //if(to.s1d == dest_1d) return;
            }
		}
	}
}

void print_path(){
    stack<string>s;
    string fnl = dest_1d;
    //cout<<"comes";
    while(parent[fnl] != fnl){
        s.push(fnl);
        fnl = parent[fnl];

    }

    while(!s.empty()){
        node nn = node(s.top());
        nn.print();
        s.pop();
    }
}

int main(){
    string start[r], strt = "";
    for(int i = 0; i <r; i++){
        string s = "";
        cin>>s;
        start[i] = s;
        strt += s;

    }
    cout<<"\n";
    node f1 = node(strt);
    bfs(f1);
    print_path();
    printf("Distance  = %d",dis[dest_1d]);
    return 0;
}
/*
1234
5678
9#AC
DEBF
*/
