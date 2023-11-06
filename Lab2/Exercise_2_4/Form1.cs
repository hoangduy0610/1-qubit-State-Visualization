using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections.Generic;

namespace Exercise_2_4
{
    public partial class Form1 : Form
    {
        private Random random = new Random();
        private List<string> paintEvents = new List<string>();
        public Form1()
        {
            this.Text = "Paint Event Demo";
            this.Paint += new PaintEventHandler(Form_Paint);
            this.MouseClick += new MouseEventHandler(Form_MouseClick_Click);
        }
        private void Form_Paint(object sender, PaintEventArgs e)
        {
            // Lấy kích thước của Form
            Graphics graphics = e.Graphics;
            Brush textBrush = new SolidBrush(Color.Black);
            Font textFont = new Font("Arial", 12);

            foreach (var paintEvent in paintEvents)
            {
                int x = random.Next(0, this.ClientSize.Width);
                int y = random.Next(0, this.ClientSize.Height);
                graphics.DrawString(paintEvent, textFont, textBrush, x, y);
            }

            textFont.Dispose();
            textBrush.Dispose();
            graphics.Dispose();
        }
        //public Form1()
        //{
        //    InitializeComponent();
        //}
        //private void Form_MouseClick(object sender, MouseEventArgs e)
        //{
            
        //}

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form_MouseClick_Click(object sender, EventArgs e)
        {
            paintEvents.Add("Paint Event");
            this.Invalidate(); // Kích hoạt lại sự kiện Paint để vẽ lại "Paint Event"
        }
    }
}
