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
    public partial class Default3 : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        

        protected void Button1_Click1(object sender, EventArgs e)
        {
            // get the input
            string zip = TextBox4.Text;

            // call the developed web service
            string url = @"http://webstrar48.fulton.asu.edu/page8/Service1.svc/wind/zip?input=" + zip;

            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();

            Index ind = JsonConvert.DeserializeObject<Index>(responsereader);

            // create object for response and store the response
            wind_Recommend recom = new wind_Recommend();
            recom.recommend = ind.recommend.recommend;
            int error = ind.recommend.error;

            // check if there is any error in the response
            if (error == 1)
            {
                TextBox5.Text = recom.recommend;
                TextBox6.Text = recom.recommend;
            }

            // else output the response
            else
            {

                TextBox5.Text = ind.index.ToString();
                TextBox6.Text = recom.recommend;
            }

        }

        protected void TextBox4_TextChanged(object sender, EventArgs e)
        {

        }

        protected void TextBox5_TextChanged(object sender, EventArgs e)
        {

        }

        protected void TextBox3_TextChanged(object sender, EventArgs e)
        {

        }

        protected void Button3_Click(object sender, EventArgs e)
        {
            // redirect to home page
            Response.Redirect("Default.aspx");
        }
    }

    // response structure
    public class wind_Recommend
    {
        public string recommend { get; set; }
        public int error { get; set; }
    }
    public class wind_Index
    {
        public double index { get; set; }
        public Recommend recommend { get; set; }
    }
}
