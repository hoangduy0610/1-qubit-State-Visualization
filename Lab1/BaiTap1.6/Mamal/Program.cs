namespace MamalManage
{
    using System;
    using Classes;

    class Program
    {
        static void Main(string[] args)
        {
            Mamal whale = new Whale("Gentle giant");
            Mamal human = new Human("Intelligent creature");

            Console.WriteLine("Whale's characteristics: " + whale.Characteristics);
            Console.WriteLine("Human's characteristics: " + human.Characteristics + "\n");

            ((Human)human).ThinkingBehaviour();
            ((Human)human).IntelligentBehaviour();
            // Console.ReadLine();
        }
    }
}