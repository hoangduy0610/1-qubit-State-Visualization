namespace MamalManage.Interfaces
{
    // Define the IThinking interface
    interface IThinking
    {
        void ThinkingBehaviour();
    }

    // Define the IIntelligent interface
    interface IIntelligent
    {
        void IntelligentBehaviour();
    }

    // Define the IAbility interface
    interface IAbility : IThinking, IIntelligent
    {

    }
}
