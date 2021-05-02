using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Web.Http;
using System.Xml;
using System.Xml.Schema;
using System.Xml.XPath;

namespace hw4partII.Controllers
{
    
    public class ValuesController : ApiController
    {

        public string result = "No Error";
       
        public  List<string> response = new List<string>();
       

        
        //Verification method to verify xml against xsd
        [HttpGet]
        [ActionName("verification")]
        public string verification([FromUri] string xsd, [FromUri] string xml)
        {
            try
            {
                // creating the appropriate settings to pass int the xml reader
                XmlReaderSettings settings = new XmlReaderSettings();
                settings.Schemas.Add(null, xsd);
                settings.ValidationType = ValidationType.Schema;
                settings.ValidationFlags |= XmlSchemaValidationFlags.ProcessInlineSchema;
                settings.ValidationFlags |= XmlSchemaValidationFlags.ProcessSchemaLocation;
                settings.ValidationFlags |= XmlSchemaValidationFlags.ReportValidationWarnings;
                settings.DtdProcessing |= DtdProcessing.Parse;
                settings.ValidationEventHandler += new ValidationEventHandler(validate);
                settings.IgnoreWhitespace = true;

                XmlReader read = XmlReader.Create(xml, settings);            
                XmlDocument document = new XmlDocument();
                document.Load(read);

            }
            catch  // if any expections occur , like incorrect xml/xsd
            {
                return "incorrect XML/XSD";
            }
            return result;  // return the result
        }

        // validate funtion to check if there is any error or missing attribute in the xml
        // and update the result variable
        private void validate(object sender, ValidationEventArgs e)
        {
            if (e.Severity == XmlSeverityType.Warning)
            {
                Console.WriteLine(" Warning" + e.Message);
                result = e.Message;
            }
            else // if there is error
            {
                Console.WriteLine(" Error message" + e.Message);
                result = e.Message;
                

            }

        }

        // xpath method to get the result of xpath query  for given xml
        [HttpGet]
        [ActionName("XPathSearch")]
        public List<string> XPathSearch([FromUri] string xml2, [FromUri] string query)
        {

            XPathDocument dx = new XPathDocument(xml2);

            XPathNavigator nav = dx.CreateNavigator();

            // get the result fo query in an iterator
            XPathNodeIterator iterator = nav.Select(query);

            // store the result in list 
            while (iterator.MoveNext())
            {
                string courseName = iterator.Current.Value;

                response.Add(courseName);
            }

            return response;

        }




    }

   
}
