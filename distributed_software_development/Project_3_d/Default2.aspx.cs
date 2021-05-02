using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Newtonsoft.Json;
using System.Net;
using System.IO;

namespace Homework3_4
{
    public partial class Default2 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            string zip = TextBox1.Text;

            // call the developed web service
            string url = @"http://webstrar48.fulton.asu.edu/page7/Service1.svc/solar/zip?input=" + zip;

            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();

            Index ind = JsonConvert.DeserializeObject<Index>(responsereader);

            // create object for response
            Recommend recom = new Recommend();
            recom.recommend = ind.recommend.recommend;
            int error = ind.recommend.error;

            // check if there is any error in the response
            if (error == 1)
            {
                TextBox2.Text = recom.recommend;
                TextBox3.Text = recom.recommend;
            }

            // else output the response
            else
            {

                TextBox2.Text = ind.index.ToString();
                TextBox3.Text = recom.recommend;
            }
        
    }

        protected void TextBox3_TextChanged(object sender, EventArgs e)
        {

        }

        protected void TextBox2_TextChanged(object sender, EventArgs e)
        {

        }

        protected void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        protected void Button2_Click(object sender, EventArgs e)
        {
            // redirect to home page
            Response.Redirect("Default.aspx");
        }
    }

    // response format
    public class Recommend
    {
        public string recommend { get; set; }
        public int error { get; set; }
    }
    public class Index
    {
        public double index { get; set; }
        public Recommend recommend { get; set; }
    }
}