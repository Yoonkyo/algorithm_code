#include <iostream>

using namespace std;

int main()
{
    int N;
    string word;
    string newword;
    cin >> N;
    for (int i=0; i<N; i++){
        cin >> word;
        if (word.size() <= 10){
            cout << word << endl;
            continue;
        }
        newword = word[0] + to_string(word.size()-2)+ word.back();
        cout << newword << endl;
    }
}
