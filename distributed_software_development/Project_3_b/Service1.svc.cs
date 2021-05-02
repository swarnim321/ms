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
        
        public Index getSunshine(string zip)
        {

            Index ind = new Index();
            Recommendation recom = new Recommendation();


            // validating zip code and getting the latitude and longitude for the zip
            string final_zip_url = "https://www.zipwise.com/webservices/zipinfo.php?key=esn9uat8x4ehsydb&zip="+zip+ "&format=json";
            HttpWebRequest request_zip = (HttpWebRequest)WebRequest.Create(final_zip_url);
            WebResponse response_zip = request_zip.GetResponse();
            Stream dataStream_zip = response_zip.GetResponseStream();
            StreamReader sreader_zip = new StreamReader(dataStream_zip);
            string responsereader_zip = sreader_zip.ReadToEnd();
            response_zip.Close();
            Console.WriteLine(response_zip);
            zip_root zr = JsonConvert.DeserializeObject<zip_root>(responsereader_zip);


            // if not a valid zip code
            if (!String.IsNullOrEmpty(zr.results.error))
            {
                ind.index = 0;
                recom.recommend = "Not a valid zip code";
                recom.error = 1;
                ind.recommend = recom;
                return ind;
            }

            //get the lat/lon for the zip
            string lat = zr.results.latitude;
            string lon = zr.results.longitude;
            

            //get the annual solar index of the area
            string url = @"https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key=41HpHgz3b2uRmoXKd2IFxO3VkP2WwjJZxuVnMgBM&lat=" + lat + "&lon=" + lon;
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();
            sun_root sr = JsonConvert.DeserializeObject<sun_root>(responsereader);

            Outputs tempOutputsObj = new Outputs();
            AvgDni tempavgObj = new AvgDni();

            tempOutputsObj = sr.outputs;
         
            tempavgObj = tempOutputsObj.avg_dni;
            var tempstr = tempavgObj.annual;
          
            ind.index = tempstr;
            
            // check if the solar index is good enough or not
            int sunshine = Convert.ToInt32(tempstr);
            if (sunshine > 5)
            {

                recom.recommend= "Sunshine index is good to set up solar farm";
                recom.error = 0;
                ind.recommend = recom;
                
            }
            else
            {

                recom.recommend = "Sunshine index is low to set up solar farm";
                recom.error = 0;
                ind.recommend = recom;
                
            }

            // return complex JSON response
            return ind;


        }
    }
}
