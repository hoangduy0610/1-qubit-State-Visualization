namespace Shape
{
    using System;
    using System.Collections.Generic;


    public abstract class Shape
    {
        public string Name;
        public abstract double CalculateArea();
        public abstract void Draw();
    }


    public class Rectangle : Shape
    {
        public double Width;
        public double Height;

        public Rectangle(string name, double width, double height)
        {
            Name = name;
            Width = width;
            Height = height;
        }

        public override double CalculateArea()
        {
            return Width * Height;
        }

        public override void Draw()
        {
            Console.WriteLine($"Ve hinh chu nhat {Name} voi chieu rong {Width} va chieu cao {Height}");
        }
    }


    public class Circle : Shape
    {
        public double Radius;

        public Circle(string name, double radius)
        {
            Name = name;
            Radius = radius;
        }

        public override double CalculateArea()
        {
            return Math.PI * Radius * Radius;
        }

        public override void Draw()
        {
            Console.WriteLine($"Ve hinh tron {Name} voi ban kinh {Radius}");
        }
    }


    public class Triangle : Shape
    {
        public double BaseLength;
        public double Height;

        public Triangle(string name, double baseLength, double height)
        {
            Name = name;
            BaseLength = baseLength;
            Height = height;
        }

        public override double CalculateArea()
        {
            return 0.5 * BaseLength * Height;
        }

        public override void Draw()
        {
            Console.WriteLine($"Ve hinh tam giac {Name} voi do dai day {BaseLength} và chieu cao {Height}");
        }
    }

  
    public class Square : Rectangle
    {
        public Square(string name, double sideLength) : base(name, sideLength, sideLength)
        {
        }
        public override void Draw()
        {
            Console.WriteLine($"Ve hinh vuong {Name} voi chieu dai canh {Height}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Nhap so luong hinh muon tao: ");
            int n = int.Parse(Console.ReadLine());

            List<Shape> shapes = new List<Shape>();

            for (int i = 1; i <= n; i++)
            {
                Console.WriteLine($"Nhap thong tin hinh thu {i}:");

                Console.Write("Loai hinh (1: Hinh chu nhat, 2: Hinh tron, 3: Hinh tam giac, 4: Hinh vuong): ");
                int type = int.Parse(Console.ReadLine());

                Console.Write("Ten hinh: ");
                string name = Console.ReadLine();

                Shape shape = null;

                switch (type)
                {
                    case 1:
                        Console.Write("Chieu rong: ");
                        double width = double.Parse(Console.ReadLine());
                        Console.Write("Chieu cao: ");
                        double height = double.Parse(Console.ReadLine());
                        shape = new Rectangle(name, width, height);
                        break;
                    case 2:
                        Console.Write("Ban kinh: ");
                        double radius = double.Parse(Console.ReadLine());
                        shape = new Circle(name, radius);
                        break;
                    case 3:
                        Console.Write("Do dai day: ");
                        double baseLength = double.Parse(Console.ReadLine());
                        Console.Write("Chieu cao: ");
                        double triHeight = double.Parse(Console.ReadLine());
                        shape = new Triangle(name, baseLength, triHeight);
                        break;
                    case 4:
                        Console.Write("Kich thuoc canh cua hinh vuong ");
                        double sideLength = double.Parse(Console.ReadLine());
                        shape = new Square(name, sideLength);
                        break;
                    default:
                        Console.WriteLine("Khong hop le.");
                        break;
                }

                if (shape != null)
                {
                    shapes.Add(shape);
                }
            }

            Console.WriteLine("Thong tin cac hinh da tao:");

            foreach (var shape in shapes)
            {
                shape.Draw();
                Console.WriteLine($"Dien Tich: {shape.CalculateArea()}");
            }
        }
    }
}