#include<iostream>
using namespace std;
int dp[300][300] = {0};
string str1 = "";
string str2 = "";
int LCS(int i, int j){
        if(dp[i][j]==0)
        {
           if(str1[i]=='\0' || str2[j]=='\0')
        {
            dp[i][j] = 0;
        }
        else if(str1[i] == str2[j])
        {
            dp[i][j] = 1+LCS(i+1, j+1);
        }
        else
        {
            dp[i][j] = max(LCS(i+1, j), LCS(i, j+1));
        }
    }

    return dp[i][j];
}


int main()
{
    cout<<"Please enter the first string ";
    cin>>str1;
    cout<<"Please enter the second string ";
    cin>>str2;
    int length1 = str1.length();
    int length2 = str2.length();
    int length = LCS(0, 0);
    char str[length+1];
    str[length] = '\0';
    int l = 0;
    int a = 0;
    int b = 0;
    //cout<<length<<endl;
    /*for(int a=0; a<10; a++)
    {
        for(int b=0; b<8; b++)
        {
            cout<<dp[a][b]<<" ";
        }
        cout<<"\n";
    }*/

    while(a<length1 && b<length2)
    {
        if(str1[a] == str2[b])
        {
            //cout<<str1[a]<<str2[b]<<endl;
            str[l] = str1[a];
            l++;
            a++;
            b++;
        }
        else
        {
            if(dp[a+1][b]>dp[a][b+1])
                a++;
            else
                b++;
        }
    }

    cout<<'\n'<<"The substring length is "<<length;

    cout<<'\n'<<"Substring is "<<str<<endl;
    return 0;
}





























