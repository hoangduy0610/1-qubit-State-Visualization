namespace MamalManage.Classes
{
    using Interfaces;
    // Create the Human class that inherits from Mamal and implements IAbility
    class Human : Mamal, IAbility
    {
        public Human(string characteristics)
        {
            Characteristics = characteristics;
        }

        public void ThinkingBehaviour()
        {
            Console.WriteLine("Hmmm, I'm Thinking bro");
        }

        public void IntelligentBehaviour()
        {
            Console.WriteLine("I'm so brilliant. I must be the best Mamal");
        }
    }

}
