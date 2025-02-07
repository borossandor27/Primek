using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Primek
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Prím szám keresés indul");
            DateTime kezdoIdo = DateTime.Now;
            int szam = 1;
            for (int i = 1; i <= 10000; i++)
            {
                if (IsPrime(i))
                {
                    Console.WriteLine(i);
                    szam++;
                }
            }
            DateTime vegIdo = DateTime.Now;
            Console.WriteLine("A prím számok száma: " + szam);
            Console.WriteLine("A program futási ideje: " + (vegIdo - kezdoIdo).TotalMilliseconds + " ms");
            Console.WriteLine("Program vége");
            Console.ReadLine();
        }
        static bool IsPrime(int number)
        {
            bool isPrime = true;
            for (int i = 2; i <= Math.Sqrt(number); i++)
            {
                if (number % i == 0)
                {
                    isPrime = false;
                    break;
                }
            }
            return isPrime;
        }
    }
}
