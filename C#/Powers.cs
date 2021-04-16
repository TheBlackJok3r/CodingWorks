using System;

namespace C__projects
{
    class Powers
    {
        static long pow(long power, long num)
        {
            if (power == 2)
            {
                return num * num;
            }
            else if (power == 3)
            {
                return num * num * num;
            }
            else if (power % 2 == 0)
            {
                return pow(power / 2, num) * pow(power / 2, num);
            }
            else if (power % 3 == 0)
            {
                return pow((power - 1) / 2, num) * pow((power - 1) / 2, num) * num;
            }
            return 0;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(pow(18, 10));
        }
    }
}
