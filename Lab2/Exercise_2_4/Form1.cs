using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Exercise_2_4
{
    public partial class Form1 : Form
    {
        private Random random = new Random();

        public Form1()
        {
            this.Text = "Paint Event Demo";
            this.Paint += new PaintEventHandler(Form_Paint);
        }
        private void Form_Paint(object sender, PaintEventArgs e)
        {
            // Lấy kích thước của Form
            int formWidth = this.ClientSize.Width;
            int formHeight = this.ClientSize.Height;

            // Tạo một Graphics để vẽ trên Form
            Graphics graphics = e.Graphics;

            // Chọn màu và font cho chuỗi vẽ
            Brush textBrush = new SolidBrush(Color.Black);
            Font textFont = new Font("Arial", 12);

            // Tạo vị trí ngẫu nhiên
            int x = random.Next(0, formWidth);
            int y = random.Next(0, formHeight);

            // Vẽ chuỗi "Paint Event" tại vị trí ngẫu nhiên
            graphics.DrawString("Paint Event", textFont, textBrush, x, y);

            // Giải phóng các đối tượng Graphics và Brush
            textFont.Dispose();
            textBrush.Dispose();
            graphics.Dispose();
        }
        //public Form1()
        //{
        //    InitializeComponent();
        //}

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
