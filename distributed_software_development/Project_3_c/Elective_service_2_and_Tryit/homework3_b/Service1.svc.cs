using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using Newtonsoft.Json;
using System.Net;
using System.IO;
using System.Web.Mvc;
using System.Web.Services;


namespace homework3_b
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    public class Service1 : IService1
    {

        
        public List<resultObject> getNews(string inputs)
        {

            // instantiate the data structure for sending the response
            Dictionary<string, List<string>> dictnews = new Dictionary<string, List<string>>();
            List<string> newsList = new List<string>();
            List<resultObject> resultList = new List<resultObject>();

            //get current date to send to the URL to get the latest news
            var dateAsString = DateTime.Now.ToString("yyyy-MM-dd");
            
            // split the input on the basis of comma
            List<string> topics = new List<string>(inputs.Split(new string[] { "," }, StringSplitOptions.None));

            // iterate for each topic and store it in the response structure
            foreach (string topic in topics)
            {
                // get the response from third party api and parse it
                string url = @"https://newsapi.org/v2/everything?q=" + topic + "&from=" + dateAsString + "&sortBy=publishedAt&apiKey=d16e830d1ea844c395cebe9f20631f70";
                HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
                WebResponse response = request.GetResponse();
                Stream dataStream = response.GetResponseStream();
                StreamReader sreader = new StreamReader(dataStream);
                string responsereader = sreader.ReadToEnd();
                response.Close();
                News_root sr = JsonConvert.DeserializeObject<News_root>(responsereader);

                List<Article> arct = new List<Article>();
                arct = sr.articles;

                // get each url and store it in the list 
                for(int i = 0; i < arct.Count; i++)
                {
                    newsList.Add(arct[i].url);
                }
                dictnews.Add(topic, newsList);
                resultObject r = new resultObject();

                // add the topic as the key and list of urls received in the newlist
                r.key = topic;
                r.value = newsList;

                // add the r object to the resultlist which is the final response
                resultList.Add(r);
                
            }

            // return the final response
            return resultList;
           


        }
    }
}
