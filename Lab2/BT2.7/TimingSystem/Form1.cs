using System;
using System.Diagnostics;
using System.Windows.Forms;

namespace TimingSystem
{
    public partial class Form1 : Form
    {
        private DateTime scheduledTime;
        private bool isScheduled = false;
        public Form1()
        {
            InitializeComponent();
            timer1.Tick += new EventHandler(CheckScheduledTime);
        }

        private void CheckScheduledTime(object sender, EventArgs e)
        {
            if (isScheduled && DateTime.Now >= scheduledTime)
            {
                timer1.Stop();
                PerformScheduledAction();
            }
        }

        private void PerformScheduledAction()
        {
            string selectedAction = comboBox1.SelectedItem.ToString();

            switch (selectedAction)
            {
                case "Shutdown":
                    Process.Start("shutdown", "/s /t 0");
                    break;
                case "Restart":
                    Process.Start("shutdown", "/r /t 0");
                    break;
                case "Log Out":
                    Process.Start("shutdown", "/l");
                    break;
                default:
                    break;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            isScheduled = false;
            timer1.Stop();
            button1.Enabled = true;
            button2.Enabled = false;
        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            scheduledTime = dateTimePicker1.Value;

            if (scheduledTime > DateTime.Now)
            {
                isScheduled = true;
                timer1.Start();
                button1.Enabled = false;
                button2.Enabled = true;
                MessageBox.Show("Scheduled", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Scheduled time must be in the future.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}