using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;



namespace Homework1B
{
    public partial class Form1 : Form
    {
        public static string image_val;
      
        public Form1()
        {
            InitializeComponent();
        }

        /*Function to navigate to the entered URL in the address bar*/
        private void Go_button_Click(object sender, EventArgs e)
        {
            webBrowser1.Navigate(textBox1.Text);
        }

        /*Function to refresh the content of the web browser*/
        private void refresh_Button_Click(object sender, EventArgs e)
        {
            webBrowser1.Refresh();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }


        /*Function for encrypt button to take the string as input from textbox and 
         * call the encrypt functionality 
         * and display the results in the textbox*/
         
        private void encrypt_button_Click(object sender, EventArgs e)
        {
            ServiceReference2.ServiceClient myclient = new ServiceReference2.ServiceClient();
            string encrypt_input = textBox2.Text;
            string result = myclient.Encrypt(encrypt_input);
            textBox3.Text = result;
        }

        /*Function for decrypt button to take the encrypted string from textbox and 
         * call the decrypt functionality 
         * and display the results in the textbox*/
        private void decrypt_button_Click(object sender, EventArgs e)
        {
            ServiceReference2.ServiceClient myclient = new ServiceReference2.ServiceClient();
            string decrypt_input = textBox3.Text;
            string result = myclient.Decrypt(decrypt_input);
            textBox5.Text = result;
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label7_Click(object sender, EventArgs e)
        {

        }

        /*Function for generate button to take the string length from textbox and 
         * call the  GetVerifierString and GetImage functionality
         * and display the image in the picture*/
        private void generate_button_Click(object sender, EventArgs e)
        {
            ServiceReference3.ServiceClient myclient = new ServiceReference3.ServiceClient();
            string image_input = textBox6.Text;
            string result = myclient.GetVerifierString(image_input);
            Stream stream_data = myclient.GetImage(result);
            var myImage = Image.FromStream(stream_data);
            pictureBox1.Image = myImage;
            image_val = result;
        }

        /*Function for verify button to check if the string entered from the image is 
         correct or not*/
        private void verify_button_Click(object sender, EventArgs e)
        {
            ServiceReference3.ServiceClient myclient = new ServiceReference3.ServiceClient();
            string verify_input = textBox8.Text;
            
            if (image_val == verify_input )
            {
                textBox9.Text = "The string entered is correct";
            }
            else
            {
                textBox9.Text = "Not the correct string. Try again";
            }
           
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
