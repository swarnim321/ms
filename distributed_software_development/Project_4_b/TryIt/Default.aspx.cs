using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Newtonsoft.Json;
using System.Net;
using System.IO;

namespace TryIt
{
    public partial class Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            // get the xml and xsd url from the input text
            string xml_url = TextBox1.Text;
            string xsd_url = TextBox2.Text;

            // call the developed web service
            string url = @"https://localhost:44306/api/Values/verification?xsd="+xsd_url +"&xml="+ xml_url;
            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();

            //display the result
            string resp = JsonConvert.DeserializeObject<string>(responsereader);
            TextBox3.Text = resp;
        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            // list to store the response
            List<string> resp = new List<string> ();

            // get the xml url and the query from the text box
            string xml_url = TextBox4.Text;
            string query = TextBox5.Text;

            // call the developed web service
            string url = @"https://localhost:44306/api/Values/XPathSearch?xml2=" + xml_url + "&query=" + query;
            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();
            
            resp = JsonConvert.DeserializeObject<List<string>>(responsereader);
            
            // Add the response on the listbox for diplay
            ListBox1.Items.Clear();
            for (int i=0;i < resp.Count; i++)
            {
                ListBox1.Items.Add(resp[i]);
                ListBox1.Items.Add("\n");
            }
            
        }
    }
}