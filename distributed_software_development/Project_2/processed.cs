using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Homework_2
{
   

    // Class to store the processed order from the airline
    class process_order_buffer
    {
        private List<processedOrder> processed_order = new List<processedOrder>(); // creating buffer to store processed order

        //Function to put order in the buffer
        public void Put(string agentName, double order, String airline)
        {
            lock (processed_order) // acquire lock to put the order in the buffer
            {
                processed_order.Add(new processedOrder(agentName, order, airline));
                Program.processed_order++;
            }
        }


        //Function to get the order from the processed buffer
        public (int, String)  Get(string agentName)
        {
            lock (processed_order)
            {
                for (int i = 0; i < processed_order.Count; i++)
                {
                    if (processed_order[i].travelAgent == agentName) // if the travel agent name same as in the buffer , return the order and delete thr order from buffer 
                    {
                        int temp = (int)processed_order[i].total_order;
                        string order= processed_order[i].air_name;
                        processed_order.RemoveAt(i);
                        return (temp,order);
                       
                    }
                }
            }

             return (0,"") ; 
        }

    }

    //class to create type of processed order buffer buffer
    public class processedOrder
    {
        public string air_name;
        public string travelAgent;
        public double total_order;
        
        public processedOrder(string agent, double amount, string air)
        {
            travelAgent = agent;
            total_order = amount;
            air_name = air;
        }
    }
}
