using System;
using System.Numerics;

namespace last_n
{
    class Program
    {

        static BigInteger raise_pow(BigInteger a, BigInteger n, BigInteger l)
        {
            if (n == 1)
                return a;
            else if (n % 2 == 0)
            {
                BigInteger s = raise_pow(a, n / 2, l) % l;
                return s * s;
            }
            else
            {
                BigInteger s = raise_pow(a, n - 1, l);
                return (a * s) % l;
            }
        }
        static BigInteger last_n(BigInteger number, BigInteger power, int n)
        {
            return raise_pow(number, power, BigInteger.Pow(10, n));
        }
        static void Main(string[] args)
        {
            Console.WriteLine(last_n(641, 1000000000000000000, 6));
            //Whole code can also be expressed like that, but it was my excercise to do it manually
            //Console.WriteLine(BigInteger.ModPow(641, 1000000000000000000, BigInteger.Pow(10, 6))); 
        }
    }
}
