using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Newtonsoft.Json;
using System.Net;
using System.IO;

namespace TryIt_3b
{
    public partial class TryIt : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            // get the input
            string zip = zip_input.Text;

            // call the developed web service
            string url = @"http://localhost:62609/Service1.svc/wind/zip?input=" + zip;
            
            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();
            
            Index ind =JsonConvert.DeserializeObject<Index>(responsereader);

            // create object for response and store the response
            Recommend recom = new Recommend();
            recom.recommend = ind.recommend.recommend;
            int error = ind.recommend.error;

            // check if there is any error in the response
            if (error == 1){
                TextBox1.Text = recom.recommend;
                output_box.Text = recom.recommend;
            }

            // else output the response
            else {

                output_box.Text = ind.index.ToString();
                TextBox1.Text = recom.recommend;
            }

        }
    }


    // response structre for the web service
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