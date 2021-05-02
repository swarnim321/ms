using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.Web.Mvc;
using homework3_b.AppClasses;

namespace homework3_b
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IService1
    {
        // Method to get the solar index of the area

        [OperationContract]
        [WebInvoke(Method = "GET", ResponseFormat = WebMessageFormat.Json, UriTemplate = "/solar/zip?input={input}")]
        Index getSunshine(string input);
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

    // response structure to extract the average anual solar index


    [DataContract]
    public class Metadata
    {
        [DataMember]
        public List<string> sources { get; set; }
    }

    [DataContract]
    public class Inputs
    {
        [DataMember]
        public string api_key { get; set; }
        [DataMember]
        public string lat { get; set; }
        [DataMember]
        public string lon { get; set; }
    }

    [DataContract]
    public class Monthly
    {
        [DataMember]
        public int jan { get; set; }
        [DataMember]
        public double feb { get; set; }
        [DataMember]
        public double mar { get; set; }
        [DataMember]
        public double apr { get; set; }
        [DataMember]
        public double may { get; set; }

        [DataMember]
        public double jun { get; set; }
        [DataMember]
        public double jul { get; set; }
        [DataMember]
        public double aug { get; set; }
        [DataMember]
        public double sep { get; set; }
        [DataMember]
        public double oct { get; set; }
        [DataMember]
        public double nov { get; set; }
        [DataMember]
        public double dec { get; set; }
    }

    [DataContract]
    public class AvgDni
    {
        [DataMember]
        public double annual { get; set; }
        [DataMember]
        public Monthly monthly1 { get; set; }
    }

    [DataContract]
    public class AvgGhi
    {
        [DataMember]
        public double annual { get; set; }
        [DataMember]
        public Monthly monthly2 { get; set; }
    }

    [DataContract]
    public class AvgLatTilt
    {
        [DataMember]
        public double annual { get; set; }
        [DataMember]
        public Monthly monthly3 { get; set; }
    }

    [DataContract]
    public class Outputs : IDisposable
    {
        [DataMember]
        public AvgDni avg_dni { get; set; }
        [DataMember]
        public AvgGhi avg_ghi { get; set; }
        [DataMember]
        public AvgLatTilt avg_lat_tilt { get; set; }

        public void Dispose() { }
    }

    [DataContract]
    public class sun_root
    {
        [DataMember]
        public string version { get; set; }
        [DataMember]
        public List<object> warnings { get; set; }
        [DataMember]
        public List<object> errors { get; set; }
        [DataMember]
        public Metadata metadata { get; set; }
        [DataMember]
        public Inputs inputs { get; set; }
        [DataMember]
        public Outputs outputs { get; set; }
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
