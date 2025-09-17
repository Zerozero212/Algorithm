#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int N=answers.size();
    vector<int> student(4,0);
    map<int,vector<int>> sol={{1,{1,2,3,4,5}},{2,{2,1,2,3,2,4,2,5}},{3,{3,3,1,1,2,2,4,4,5,5}}};
    
    for (int i=0; i<N; ++i){
        if (answers[i]==sol[1][i%5]){
            student[1]++;
        }
        if (answers[i]==sol[2][i%8]){
            student[2]++;
        }
        if (answers[i]==sol[3][i%10]){
            student[3]++;
        }
    }
    auto max_num = max_element(student.begin(),student.end());
    for (int i=1;i<student.size();++i){
        if (*max_num==student[i]){
            answer.push_back(i);
        }
    }
    
    return answer;
}