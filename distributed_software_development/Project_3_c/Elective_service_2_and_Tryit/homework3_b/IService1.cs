using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.Web.Mvc;

namespace homework3_b
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        // Method to get the solar index of the area

        [OperationContract]
        [WebInvoke(Method = "GET", ResponseFormat = WebMessageFormat.Json, UriTemplate = "/news/{inputs}")]
        //Dictionary<string, List<string>> getSunshine(string inputs);
        List<resultObject> getNews(string inputs);
    }


    // Use a data contract as illustrated in the sample below to add composite types to service operations.
    [DataContract]


    // response structure for verifying the zip code
   



    //************************************************************************************************

    // response structure to extract the average anual solar index


    public class Source
    {
        public object id { get; set; }
        public string name { get; set; }
    }

    public class Article
    {
        public Source source { get; set; }
        public string author { get; set; }
        public string title { get; set; }
        public string description { get; set; }
        public string url { get; set; }
        public string urlToImage { get; set; }
        public DateTime publishedAt { get; set; }
        public string content { get; set; }
    }

    public class News_root
    {
        public string status { get; set; }
        public int totalResults { get; set; }
        public List<Article> articles { get; set; }
    }

    //************************************************************************************************


    // response structure for the current web service to be returned
    [DataContract]
    public class Recommendation
    {
        [DataMember]
        public string recommend { get; set; }
        [DataMember]
        public int error { get; set; }
    }

    [DataContract]
    public class Index
    {
        //[DataMember]
        //public Recommendation recommend { get; set; }
        [DataMember]
        public double index { get; set; }

        
        
    }
    [DataContract]
    public class resultObject
    {
        [DataMember]
        public string key { get; set; }
        [DataMember]
        public List<string> value { get; set; }
    }

    
}
