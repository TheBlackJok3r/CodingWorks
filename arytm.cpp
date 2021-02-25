#include <iostream>
#include <fstream>
#include <stdio.h>
#include <sstream>

using namespace std;

string temp;

int rek(string s, int k)
{
    int score, a, b;
    if(s[k-1]=='(' && s[k+1]==')')
    {
        int t=s[k]-'0';
        s.replace(k-1,3, to_string(t));
        temp=s;
    }
    else if(s[k]=='(')
    {
        rek(s, k+1);
    }
    else
    {
        int a=s[k]-'0';

        if(s[k+1]=='+')
        {
            if(s[k+2]=='(')
            {  
                b=rek(s, k+2);
            }
            else
            {
                b=s[k+2]-'0';
            }
            score=a+b;
        }


        if(s[k+1]=='-')
        {
            if(s[k+2]=='(')
            {
                b=rek(s, k+2);
            }
            else
            {
                b=s[k+2]-'0';
            }
            score=a-b;
        }

        if(s[k+3]==')')
        {
            s.replace(k-1,5, to_string(score));
            temp=s;
        }
        else
        {
            s.replace(k,3, to_string(score));
            temp=s;
        }
        return score;
    }
    return 0;
}




int main()
{
    string text, result;
    fstream f;
    f.open("test.txt");
    f >> text;
    string A[text.length()];
    int a,b,score=text[0]-'0',i=0;
    while(i!=text.length())
    {
        if(to_string(score)==text)
        {
            break;
        }
        else if(text[i]=='(')
        {
            cout<<text <<" ";
            rek(text, i+1);
            i=-1;
            text=temp;
        }
        else if(text[i]=='+')
        {
            a=text[i-1]-'0';
            if(text[i+1]=='(')
            {
                b=rek(text, i+2);
            }
            else
            {
                b=text[i+1]-'0';
            }
            score=a+b;
            text.replace(i-1,3, to_string(score));
            i=0;
        }
        else if(text[i]=='-')
        {
            a=text[i-1]-'0';
            if(text[i+1]=='(')
            {
                b=rek(text, i+2);
            }
            else
            {
                b=text[i+1]-'0';
            }
            score=a-b;
            text.replace(i-1,3, to_string(score));
            i=0;
        }
        i++;
    }
    
    cout << text;
}