using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Xml;

namespace hw4part1
{
    public partial class Default : System.Web.UI.Page
    {
        public XmlDocument doc = new XmlDocument();
        public XmlNode node;
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void Button1_Click(object sender, EventArgs e)
        {
            string file = "http://webstrar48.fulton.asu.edu/page6/restaurants.xml";   // making the xml as default input
            if (!String.IsNullOrEmpty(TextBox1.Text))   // if the user gives the input , take that xml as file and load it
            {
                file = TextBox1.Text;
            }

            // load the file
            doc.Load(file);
            XmlNode root = doc.DocumentElement;
            ListBox1.Items.Clear();
            OutputNode(root);   // call the output function to iterate through xml

        }

        void OutputNode(XmlNode node)    // recursive
        {
            if (node == null)
                System.Environment.Exit(1);

            //Console.WriteLine("Type={0}\tName={1}\tValue={2}", node.NodeType, node.Name, node.Value);
            if (node.NodeType.ToString() == "Text")
            {
                ListBox1.Items.Add(node.Value);
            }
            if (node.Name.ToString() == "Restaurant")
            {
                ListBox1.Items.Add("===================");
                ListBox1.Items.Add("Delivery : " + node.Attributes["Delivery"].Value);
            }

            if (node.Name.ToString() == "Website")
            {
                if (node.Attributes["facebook"] != null)
                {
                    ListBox1.Items.Add("facebook : " + node.Attributes["facebook"].Value);
                }
            }




            if (node.HasChildNodes)
            {

                XmlNodeList children = node.ChildNodes;
                foreach (XmlNode child in children)
                    OutputNode(child);
            }

        }
    }
}