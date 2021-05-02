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
        
        public Index getwind(string zip)
        {

            Index ind = new Index();
            Recommendation recom = new Recommendation();
            List<double> windList = new List<double>();


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
            

            //get the annual wind index of the area
            string url = "http://api.openweathermap.org/data/2.5/forecast?lat="+lat+"&lon="+lon+"&appid=ea10281789590013ee0e24ca2e40f2cd";
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(url);
            WebResponse response = request.GetResponse();
            Stream dataStream = response.GetResponseStream();
            StreamReader sreader = new StreamReader(dataStream);
            string responsereader = sreader.ReadToEnd();
            response.Close();
            wind_Root wr = JsonConvert.DeserializeObject<wind_Root>(responsereader);

            List <List1> tempList1Object = new List<List1>();
            tempList1Object = wr.list;
            Wind wind = new Wind();
            
            // add the daily windspeed to the windlist one by one
            
            for (int i = 0;i< tempList1Object.Count; i++)
            {
                wind = tempList1Object[i].wind;
                windList.Add(wind.speed);
            }

            // calculate the total windspeed by the total length of the list to get the average 
            double speed = 0;
            for (int i = 0; i < windList.Count; i++)
            {
                speed += windList[i];
            }
            double average_speed = speed / windList.Count;
            ind.index = average_speed;

            // check if the wind index is good enough or not
            int wind_speed = Convert.ToInt32(average_speed);
            if (wind_speed > 2.5)
            {

                recom.recommend= "wind   index is good to set up wind farm";
                recom.error = 0;
                ind.recommend = recom;
                
            }
            else
            {

                recom.recommend = "wind  index is low to set up wind farm";
                recom.error = 0;
                ind.recommend = recom;
                
            }

            // return complex JSON response
            return ind;


        }
    }
}
