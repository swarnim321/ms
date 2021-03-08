using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsSOAPClient
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label2_Click(object sender, EventArgs e)
        {

        }


        /*Function to call the service of counting the vowel and display 
         * in the output textbox*/
        private void vowels_Button_Click(object sender, EventArgs e)
        {
            ServiceReference1.WebService1SoapClient myclient = new ServiceReference1.WebService1SoapClient("WebService1Soap");
            string vowels_input = input_Textbox.Text ;
            int result = myclient.vowels(vowels_input);
            output_Textbox.Text = result.ToString();

        }


        /*Function to call the service of counting the uppercase letters and display 
         * in the output textbox*/
        private void count_Uppercase_button_Click(object sender, EventArgs e)
        {
            ServiceReference1.WebService1SoapClient myclient = new ServiceReference1.WebService1SoapClient("WebService1Soap");
            string uppercase_input = input_Textbox.Text;
            int result = myclient.uppercase(uppercase_input);
            output_Textbox.Text = result.ToString();
        }


        /*Function to call the service of reversing the string entered and display 
         * in the output textbox*/
        private void reverse_Button_Click(object sender, EventArgs e)
        {
            ServiceReference1.WebService1SoapClient myclient = new ServiceReference1.WebService1SoapClient("WebService1Soap");
            string reverse_input = input_Textbox.Text;
            string result = myclient.reverse(reverse_input);
            output_Textbox.Text = result;
        }
    }
}
