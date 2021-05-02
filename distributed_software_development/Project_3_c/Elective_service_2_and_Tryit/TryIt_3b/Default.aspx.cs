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
            // get the input and replace any spaces in the list
            string topics = zip_input.Text;
            topics = topics.Replace(" ,", ",");
            topics = topics.Replace(", ", ",");
            topics = topics.Replace(" ", "_");


            List<resultObject> listdictnews1 = new List<resultObject>();

            // call the developed web service
            string url = @"http://localhost:62610/Service1.svc/news/" + topics;
            
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
            ListBox1.Items.Clear();
            for (int i = 0; i < listdictnews1.Count; i++)
            {

                ListBox1.Items.Add(listdictnews1[i].key);
                for (int j = 0; j < listdictnews1[i].value.Count; j++)
                {
                    ListBox1.Items.Add(listdictnews1[i].value[j]);
                }
                
            }

            

    }

        protected void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        protected void ListBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }

    // response structre for the web service
    public class resultObject
    {
        
        public string key { get; set; }
       
        public List<string> value { get; set; }
    }

    
   
}