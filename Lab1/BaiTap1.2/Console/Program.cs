using System;

public class Fraction : IComparable<Fraction>
{
    private int numerator;
    private int denominator;

    public Fraction(int numerator, int denominator)
    {
        if (denominator == 0)
            throw new ArgumentException("Denominator cannot be zero.");

        this.numerator = numerator;
        this.denominator = denominator;
        Simplify();
    }

    public int Numerator
    {
        get { return numerator; }
    }

    public int Denominator
    {
        get { return denominator; }
    }

    public static Fraction operator +(Fraction a, Fraction b)
    {
        int newNumerator = a.numerator * b.denominator + b.numerator * a.denominator;
        int newDenominator = a.denominator * b.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    public static Fraction operator -(Fraction a, Fraction b)
    {
        int newNumerator = a.numerator * b.denominator - b.numerator * a.denominator;
        int newDenominator = a.denominator * b.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    public static Fraction operator *(Fraction a, Fraction b)
    {
        int newNumerator = a.numerator * b.numerator;
        int newDenominator = a.denominator * b.denominator;
        return new Fraction(newNumerator, newDenominator);
    }

    public static Fraction operator /(Fraction a, Fraction b)
    {
        if (b.numerator == 0)
            throw new DivideByZeroException("Cannot divide by zero.");

        int newNumerator = a.numerator * b.denominator;
        int newDenominator = a.denominator * b.numerator;
        return new Fraction(newNumerator, newDenominator);
    }

    public static bool operator ==(Fraction a, Fraction b)
    {
        if (ReferenceEquals(a, b))
            return true;
        if ((object)a == null || (object)b == null)
            return false;

        return a.numerator == b.numerator && a.denominator == b.denominator;
    }

    public static bool operator !=(Fraction a, Fraction b)
    {
        return !(a == b);
    }

    public static bool operator <(Fraction a, Fraction b)
    {
        return (a.numerator * b.denominator) < (b.numerator * a.denominator);
    }

    public static bool operator >(Fraction a, Fraction b)
    {
        return (a.numerator * b.denominator) > (b.numerator * a.denominator);
    }

    public static implicit operator Fraction(int value)
    {
        return new Fraction(value, 1);
    }

    public static explicit operator double(Fraction fraction)
    {
        return (double)fraction.numerator / fraction.denominator;
    }

    private void Simplify()
    {
        int gcd = GCD(numerator, denominator);
        numerator /= gcd;
        denominator /= gcd;
    }

    private int GCD(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public int CompareTo(Fraction other)
    {
        double thisValue = (double)numerator / denominator;
        double otherValue = (double)other.numerator / other.denominator;
        return thisValue.CompareTo(otherValue);
    }

    public override string ToString()
    {
        return numerator + "/" + denominator;
    }
}

class Program
{
    static void Main(string[] args)
    {
        Fraction[] fractions = new Fraction[]
        {
            new Fraction(3, 4),
            new Fraction(1, 2),
            new Fraction(5, 6),
            new Fraction(2, 3)
        };

        Console.WriteLine("Fractions before sorting:");
        foreach (Fraction fraction in fractions)
        {
            Console.WriteLine(fraction);
        }

        Array.Sort(fractions);

        Console.WriteLine("\nFractions after sorting:");
        foreach (Fraction fraction in fractions)
        {
            Console.WriteLine(fraction);
        }
    }
}