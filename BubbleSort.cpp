#include <iostream>
#include <algorithm>
#include <ctime>
using namespace std;

int n=100;
int A[100];

void RandGen()
{
  srand(time(NULL));
  for(int i=0; i<n; i++)
  {
  A[i]=rand()%1000;
  }
}

void ShowTab()
{
    for (int i=0; i<n; i++)
  {
    cout << A[i] << " ";
  }
}

void BubbleSort0()
{
  for (int i=0; i<n-1; i++)
  {
    for(int l=0; l<n-1; l++)
    {
      if(A[l]>A[l+1])
      {
        swap(A[i], A[i+1]);
      }
    }
   
}
}

void BubbleSort1a()
{
  int temp;
  for (int i=0; i<n-1; i++)
  {
    for(int l=0; l<n-1-i; l++)
    {
      if(A[l]>A[l+1])
      {
        temp=A[l];
        A[l]=A[l+1];
        A[l+1]=temp;
      
      }
    }
   
}
}

void BubbleSort1b()
{
  int temp;
  for (int i=0; i<(n-1)/2; i++)
    {
        int d=1;
        for(int j=i; j<n-1-i; j=j+d)
        {
            if(A[j]>A[j+1])
            swap(A[j], A[j+1]);

            if (A[n-j-2]>A[n-j-1])
            swap(A[n-j-2], A[n-j-1]);
        }
    }   
}

void BubbleSort2()
{
    for (int i=0; i<n-1; i++)
    {
        bool DidSwap=false;
        for(int j=0; j<n-1-i; j++)
        {
            if(A[j]>A[j+1])
            {
              swap(A[j], A[j+1]);
              DidSwap=true;
            }
        }
        if(DidSwap==false)
        break;
    }
}

void AlaBubbleSort3()
{
  int first=0, firsttemp, last=n-1, lasttemp;
    for (int i=0; i<(n-1)/2; i++)
    {
      bool DidSwap=false;
        for(int j=first; j<last; j++)
        {
            if(A[j]>A[j+1])
              {
                swap(A[j], A[j+1]);
                lasttemp=j;
                DidSwap=true;
              }

            if (A[last-(j-first)-1]>A[last-(j-first)])
              {
                swap(A[last-(j-first)-1], A[last-(j-first)]);
                firsttemp =last-(j-first)-1;
                DidSwap=true;
              }

        }
        if(DidSwap==false)
          break;
        first=firsttemp;
        last=lasttemp;    
    }   
}


void BubbleSort3()
{
  int d=1, first=0, last=n-2, lasttemp;
  for (int i=0; i<(n-1); i++)
    {
        for(int j=first; j!=last+d; j=j+d)
        {
            if(A[j]>A[j+1])
            {
              lasttemp=j;
              swap(A[j],A[j+1]);
            } //Wykonywanych maksymalnie n niepotrzebnych porównań przez zwrot j+1, natomiast gdy uzależnię to od d, wychodzi całkiem zabawna rzecz. Na razie nie mam pomysłu na naprawę tego.
        }

        last=lasttemp;
        d=d*-1;
        swap(first,last);
    }   
}

int main() {

  RandGen();
  ShowTab();
  cout << endl;
  cout << endl;
  cout << endl;
  cout << endl;
  BubbleSort3();
  ShowTab();
}