using System;
using System.Collections.Generic;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int[] integers = { 5, 2, 9, 1, 7 };
        Console.WriteLine("So lon nhat trong day so nguyen: " + FindMax(integers));
        Console.WriteLine("So nho nhat trong day so nguyen: " + FindMin(integers));

        double[] doubles = { 3.14, 1.618, 2.718, 0.577 };
        Console.WriteLine("So lon nhat trong day so thuc: " + FindMax(doubles));
        Console.WriteLine("So nho nhat trong day so thuc: " + FindMin(doubles));

        string[] strings = { "apple", "banana", "cherry", "date" };
        Console.WriteLine("Chuoi dai nhat trong day chuoi: " + FindMax(strings));
        Console.WriteLine("Chuoi ngan nhat trong day chuoi: " + FindMin(strings));
    }

    static T FindMax<T>(IEnumerable<T> collection) where T : IComparable<T>
    {
        if (collection.Any())
        {
            return collection.Max();
        }
        throw new InvalidOperationException("Day rong");
    }

    static T FindMin<T>(IEnumerable<T> collection) where T : IComparable<T>
    {
        if (collection.Any())
        {
            return collection.Min();
        }
        throw new InvalidOperationException("Day rong");
    }
}