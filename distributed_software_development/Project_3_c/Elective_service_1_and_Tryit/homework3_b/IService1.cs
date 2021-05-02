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
        [WebInvoke(Method = "GET", ResponseFormat = WebMessageFormat.Json, UriTemplate = "/wind/zip?input={input}")]
        Index getwind(string input);
    }


    // Use a data contract as illustrated in the sample below to add composite types to service operations.
    [DataContract]


    // response structure for verifying the zip code
    public class Cities
    {
        [DataMember]
        public string city { get; set; }

        [DataMember]
        public string preferred { get; set; }


    }

    [DataContract]

    public class Results
    {
        [DataMember]
        public string zip { get; set; }
        [DataMember]
        public List<Cities> cities { get; set; }
        [DataMember]
        public string county { get; set; }

        [DataMember]
        public string state { get; set; }
        [DataMember]
        public string country { get; set; }
        [DataMember]
        public string area_code { get; set; }
        [DataMember]
        public string fips { get; set; }
        [DataMember]
        public string time_zone { get; set; }
        [DataMember]
        public string daylight_savings { get; set; }
        [DataMember]
        public string latitude { get; set; }
        [DataMember]
        public string longitude { get; set; }
        [DataMember]
        public string type { get; set; }
        [DataMember]
        public string population { get; set; }
        [DataMember]
        public string error { get; set; }

    }

    [DataContract]
    public class zip_root
    {
        [DataMember]
        public Results results { get; set; }
    }



    //************************************************************************************************

    // response structure to extract the average anual wind index

   

    [DataContract]
    public class Main
    {
        [DataMember]
        public double temp { get; set; }
        [DataMember]
        public double feels_like { get; set; }
        [DataMember]
        public double temp_min { get; set; }
        [DataMember]
        public double temp_max { get; set; }
        [DataMember]
        public int pressure { get; set; }
        [DataMember]
        public int sea_level { get; set; }
        [DataMember]
        public int grnd_level { get; set; }
        [DataMember]
        public int humidity { get; set; }
        [DataMember]
        public double temp_kf { get; set; }
    }

    [DataContract]
    public class Weather
    {
        [DataMember]
        public int id { get; set; }
        [DataMember]
        public string main { get; set; }
        [DataMember]
        public string description { get; set; }
        [DataMember]
        public string icon { get; set; }
    }

    [DataContract]
    public class Clouds
    {
        [DataMember]
        public int all { get; set; }
    }

    [DataContract]
    public class Wind
    {
        [DataMember]
        public double speed { get; set; }
        [DataMember]
        public int deg { get; set; }
    }

    [DataContract]
    public class Sys
    {
        [DataMember]
        public string pod { get; set; }
    }

    [DataContract]
    public class List1
    {
        [DataMember]
        public int dt { get; set; }
        [DataMember]
        public Main main { get; set; }
        [DataMember]
        public List<Weather> weather { get; set; }
        [DataMember]
        public Clouds clouds { get; set; }
        [DataMember]
        public Wind wind { get; set; }
        [DataMember]
        public int visibility { get; set; }
        [DataMember]
        public double pop { get; set; }
        [DataMember]
        public Sys sys { get; set; }
        [DataMember]
        public string dt_txt { get; set; }
    }

    [DataContract]
    public class Coord
    {
        [DataMember]
        public double lat { get; set; }
        [DataMember]
        public double lon { get; set; }
    }

    [DataContract]
    public class City
    {
        [DataMember]
        public int id { get; set; }
        [DataMember]
        public string name { get; set; }
        [DataMember]
        public Coord coord { get; set; }
        [DataMember]
        public string country { get; set; }
        [DataMember]
        public int population { get; set; }
        [DataMember]
        public int timezone { get; set; }
        [DataMember]
        public int sunrise { get; set; }
        [DataMember]
        public int sunset { get; set; }
    }

    [DataContract]
    public class wind_Root
    {
        [DataMember]
        public string cod { get; set; }
        [DataMember]
        public int message { get; set; }
        [DataMember]
        public int cnt { get; set; }
        [DataMember]
        public List<List1> list { get; set; }
        [DataMember]
        public City city { get; set; }
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
        [DataMember]
        public Recommendation recommend { get; set; }
        [DataMember]
        public double index { get; set; }
        
        
    }
}
