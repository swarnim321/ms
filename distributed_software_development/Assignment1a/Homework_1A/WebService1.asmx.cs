using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Services;

namespace Homework_1A
{
    /// <summary>
    /// Summary description for WebService1
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    // [System.Web.Script.Services.ScriptService]
    public class WebService1 : System.Web.Services.WebService
    {

        
        
        [WebMethod]
        public int vowels(string strng)
        {
            int count = 0;
            char[] arr = { 'a', 'e', 'i', 'o', 'u' };

            for (int counter = 0; counter < strng.Length; counter++)
            {
                if (arr.Contains(strng[counter]) || arr.Contains(char.ToLower(strng[counter])))
                {
                    count += 1;
                }
            }
            return count;
        }

        [WebMethod]
         public int uppercase(string strng)
        {
            int count = 0;

            for (int i=0; i<strng.Length; i++)
            {
                if (char.IsUpper(strng[i]))
                {
                    count++;
                }
            }
            return count;
        }

        [WebMethod]
        public string reverse(string strng)
        {
            char[] charArray = strng.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
