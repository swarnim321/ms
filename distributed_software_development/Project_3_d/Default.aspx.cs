using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using Newtonsoft.Json;
using System.Net;
using System.IO;

namespace Homework3_4
{
    public partial class Default : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            // get the input

        }
        protected void TextBox3_TextChanged(object sender, EventArgs e)
        {

        }





        protected void Button4_Click(object sender, EventArgs e)
        {
            // redirect to solar service try it page
            Response.Redirect("Default2.aspx");


        }









        protected void Button5_Click(object sender, EventArgs e)
        {
            // redirect to wind service try it page
            Response.Redirect("Default3.aspx");
        }

        protected void Button6_Click(object sender, EventArgs e)
        {
            // redirect to news servie try it page
            Response.Redirect("Default4.aspx");
        }
    }
   }