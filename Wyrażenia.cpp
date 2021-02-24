#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>

using namespace std;

int rek(string s, int k)
{
    int score, a, b;

    if(s[k]=='(')
    {
        rek(s, k+1);
    }
    else
    {
        int a=int(s[1]);

        if(s[k+1]=='+')
        {
            if(s[k+1]=='(')
            {
                b=rek(s, k+2);
            }
            else
            {
                b=s[k+2];
            }
        }


        else if(s[k+1]=='-')
        {
            if(s[k+1]=='(')
            {
                b=rek(s, k+2);
            }
            else
            {
                b=s[k+2];
            }
        }


        else if(s[k+1]=='*')
        {
            if(s[k+1]=='(')
            {
                int b=rek(s, k+2);
            }
            else
            {
                b=s[k+2];
            }
        }
    }
    return score=a*b;
}

int main()
{
    string text, result;
    fstream f;
    f.open("test.txt");
    f >> text;
    string A[text.length()];
    int a,b,score;
    for (int i=0; i<text.length(); i++)
    {
        
    }
}