using System;

class Thermometer
{
    private double temperature;

    public event EventHandler TemperatureChanged;

    public double Temperature
    {
        get { return temperature; }
        set
        {
            double roundedValue = Math.Round(value, 1); // Làm tròn giá trị nhiệt độ đến số thập phân thứ nhất
            if (roundedValue != temperature)
            {
                temperature = roundedValue;
                OnTemperatureChanged();
            }
        }
    }

    protected virtual void OnTemperatureChanged()
    {
        TemperatureChanged?.Invoke(this, EventArgs.Empty);
    }
}

class TemperatureDisplay
{
    public void Subscribe(Thermometer thermometer)
    {
        thermometer.TemperatureChanged += HandleTemperatureChanged;
    }

    public void HandleTemperatureChanged(object sender, EventArgs e)
    {
        if (sender is Thermometer thermometer)
        {
            Console.WriteLine("New temperature: " + thermometer.Temperature);
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        Thermometer thermometer = new Thermometer();
        TemperatureDisplay display = new TemperatureDisplay();

        display.Subscribe(thermometer);

        Random random = new Random();
        for (int i = 0; i < 5; i++)
        {
            double newTemperature = random.NextDouble() * 100;
            thermometer.Temperature = newTemperature;
            System.Threading.Thread.Sleep(1000);
        }
    }
}
