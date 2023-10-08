using System;
using System.IO;
using System.Text;

namespace FolderPath
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.InputEncoding = Encoding.UTF8;
            Console.OutputEncoding = Encoding.UTF8;

            Console.Write("Nhập đường dẫn thư mục: ");
            string folderPath = Console.ReadLine();

            if (Directory.Exists(folderPath))
            {
                string[] subDirectories = Directory.GetDirectories(folderPath);

                if (subDirectories.Length > 0)
                {
                    Console.WriteLine("Các thư mục con trong thư mục chính:");
                    foreach (string subDirectory in subDirectories)
                    {
                        Console.WriteLine(Path.GetFileName(subDirectory));
                    }
                }
                else
                {
                    Console.WriteLine("Thư mục chính không có thư mục con.");
                }
            }
            else
            {
                Console.WriteLine("Đường dẫn thư mục không tồn tại.");
            }
        }
    }
}