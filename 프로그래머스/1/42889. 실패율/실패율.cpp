#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(int N, vector<int> stages) {
    vector<int> answer;
    vector<vector<float>> user(N+1,vector<float>(2,0));

    for (int num: stages) {
        if (num<=N){
            user[num][0]+=1;    
        }
        if (num>N){
            num=N;
        }
        for (int j=1;j<=num;++j){
            user[j][1]+=1;
        }
    }
    for (int i=1;i<=N;++i){
        if (user[i][1] == 0) user[i][0] = 0;  
        else user[i][0] /= user[i][1];
    }
    for (int i=1;i<=N;++i){
        answer.push_back(i);
    }

    for (int i=0; i<N-1; ++i) {
        int idx = i;
        for (int j=i+1; j<N; ++j) {
            if (user[answer[j]][0] > user[answer[idx]][0]) {
                idx = j;
            }
            else if (user[answer[j]][0] == user[answer[idx]][0] && answer[j] < answer[idx]) {
                idx = j;
            }
        }
        if (idx != i) swap(answer[i], answer[idx]);
    }

    return answer;
}
