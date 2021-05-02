using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Newtonsoft.Json;
using System.Net;
using System.IO;
using System.Web.Caching;

namespace Homework5
{
    public partial class Default : System.Web.UI.Page
    {
        public static string session_variable = "";
      
        protected void Page_Load(object sender, EventArgs e)
        {
            
            session_variable = "";

        }

        protected void Button1_Click(object sender, EventArgs e)
        {

            // Taking inpit as zip and storing it in the session variable and also passing in the urls
            string zip = TextBox1.Text;
            if (Session["zip"] == null)
            {
                Session["zip"] = zip + "";
            }
            else
            {
                Session["zip"] = Session["zip"].ToString() + "," + zip;
            }
            TextBox8.Text = Session["zip"].ToString();

            // call the developed web service for solar index
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


            // call the developed web services for wind index
            string url_wind = @"http://webstrar48.fulton.asu.edu/page8/Service1.svc/wind/zip?input=" + zip;

            // parse the response
            HttpWebRequest request_wind = (HttpWebRequest)WebRequest.Create(url_wind);
            WebResponse response_wind = request_wind.GetResponse();
            Stream dataStream_wind = response_wind.GetResponseStream();
            StreamReader sreader_wind = new StreamReader(dataStream_wind);
            string responsereader_wind = sreader_wind.ReadToEnd();
            response_wind.Close();

            Index ind_wind = JsonConvert.DeserializeObject<Index>(responsereader_wind);

            // create object for response and store the response
            wind_Recommend recom_wind = new wind_Recommend();
            recom_wind.recommend = ind_wind.recommend.recommend;
            int error_wind = ind_wind.recommend.error;

            // check if there is any error in the response
            if (error_wind == 1)
            {
                TextBox5.Text = recom_wind.recommend;
                TextBox6.Text = recom_wind.recommend;
            }

            // else output the response
            else
            {

                TextBox5.Text = ind_wind.index.ToString();
                TextBox6.Text = recom_wind.recommend;
            }


            List<resultObject> listdictnews1 = new List<resultObject>();

            // call the developed web service to get the news related to solar energy
            string url_news_solar = @"http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/solar";

            // parse the response
            HttpWebRequest request_news_solar = (HttpWebRequest)WebRequest.Create(url_news_solar);
            WebResponse response_news_solar = request_news_solar.GetResponse();

            Stream dataStream_news_solar = response_news_solar.GetResponseStream();
            StreamReader sreader_news_solar = new StreamReader(dataStream_news_solar);
            string responsereader_news_solar = sreader_news_solar.ReadToEnd();

            response.Close();

            // store the response in the respective format
            listdictnews1 = JsonConvert.DeserializeObject<List<resultObject>>(responsereader_news_solar);

            // Display the items in the listbox in the display
            ListBox1.Items.Clear();
            for (int i = 0; i < listdictnews1.Count; i++)
            {

                ListBox1.Items.Add(listdictnews1[i].key);
                for (int j = 0; j < listdictnews1[i].value.Count; j++)
                {
                    ListBox1.Items.Add(listdictnews1[i].value[j]);
                }

            }

            List<resultObject> listdictnews2 = new List<resultObject>();

            // call the developed web service to get the news related to wind energy
            string url_news_wind = @"http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/wind";

            // parse the response
            HttpWebRequest request_news_wind = (HttpWebRequest)WebRequest.Create(url_news_wind);
            WebResponse response_news_wind = request_news_wind.GetResponse();

            Stream dataStream_news_wind = response_news_wind.GetResponseStream();
            StreamReader sreader_news_wind = new StreamReader(dataStream_news_wind);
            string responsereader_news_wind = sreader_news_wind.ReadToEnd();

            response_news_wind.Close();

            // store the response in the respective format
            listdictnews2 = JsonConvert.DeserializeObject<List<resultObject>>(responsereader_news_wind);

            // Display the items in the listbox in the display

            for (int i = 0; i < listdictnews2.Count; i++)
            {

                ListBox1.Items.Add(listdictnews2[i].key);
                for (int j = 0; j < listdictnews2[i].value.Count; j++)
                {
                    ListBox1.Items.Add(listdictnews2[i].value[j]);
                }

            }

           // display the cached value in the listbox

            if (ListBox3.Items.Count == 0)
            {
                Cache["last_zip"] = zip;
                Cache["solar_index"] = ind.index;
                Cache["wind_index"] = ind_wind.index;

                ListBox3.Items.Add("Last zip searched: " + Cache["last_zip"].ToString());
                ListBox3.Items.Add("Last solar Index: " + Cache["solar_index"].ToString());
                ListBox3.Items.Add("Last wind index: " + Cache["wind_index"].ToString());

            }
            else
            {
                ListBox3.Items.Clear();
                ListBox3.Items.Add("Last zip searched: " + Cache["last_zip"].ToString());
                ListBox3.Items.Add("Last solar Index: " + Cache["solar_index"].ToString());
                ListBox3.Items.Add("Last wind index: " + Cache["wind_index"].ToString());
                Cache["last_zip"] = zip;
                Cache["solar_index"] = ind.index;
                Cache["wind_index"] = ind_wind.index;
            }


            }
    


            protected void Button3_Click(object sender, EventArgs e)
        {
            // get the input and replace any spaces in the list
            string topics = TextBox7.Text;
            topics = topics.Replace(" ,", ",");
            topics = topics.Replace(", ", ",");
            topics = topics.Replace(" ", "_");


            List<resultObject> listdictnews1 = new List<resultObject>();

            // call the developed web service
            string url = @"http://webstrar48.fulton.asu.edu/page9/Service1.svc/news/" + topics;

            // parse the response
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();

            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();

            response.Close();

            // store the response in the respective format
            listdictnews1 = JsonConvert.DeserializeObject<List<resultObject>>(responsereader);

            // Display the items in the listbox in the display
            ListBox2.Items.Clear();
            for (int i = 0; i < listdictnews1.Count; i++)
            {

                ListBox2.Items.Add(listdictnews1[i].key);
                for (int j = 0; j < listdictnews1[i].value.Count; j++)
                {
                    ListBox2.Items.Add(listdictnews1[i].value[j]);
                }

            }
        }

        
    }

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

    public class resultObject
    {

        public string key { get; set; }

        public List<string> value { get; set; }
    }
}