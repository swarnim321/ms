using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Homework_2
{
    class OrderProcessing
    {
        public  Int32 rejected_order = 0;  // get the count of rejected order
        public void orderFunc(OrderObject order)
        {
            // get the card number for the order
            int cardNo = order.getCardNum();

            // check if the card is vald
            if (cardNo >= 5000 && cardNo <= 7000)
            {
                
                // get the total amount of the order 
                double orderTotal = order.getUnitPrice() * order.getAmount() * .081;
                string recev_id = order.getReceiverID();
                
                // order valid , so put the order in the confirmation buffer
                Program.confirmed_order.Put(order.getSenderID(), orderTotal, recev_id);   
            }
            else
            {
                rejected_order++; // if order rejected then increament the count of rejected order
                
            }
        }

        // Function to get the count of rejected orders
        public int getRejected_order()
        {
            return rejected_order;
        }
    }
}

