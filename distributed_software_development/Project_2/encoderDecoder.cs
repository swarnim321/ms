using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Security.Cryptography;
using System.Threading;

namespace Homework_2
{
    class encoderDecoder
    {
        //Function to encrypt the order
        public static string encrypt(OrderObject oo)
        {
            
            string encrypted = oo.getSenderID() + ":" + oo.getCardNum() + ":" + oo.getReceiverID() + ":" + oo.getAmount() + ":" + oo.getUnitPrice();
            return encrypted;

        }

        // Function to decrypt the order
        public static OrderObject decrypt(String s)
        {
            
            String[] items = s.Split(':');
            OrderObject order = new OrderObject(items[0], Convert.ToInt32(items[1]), items[2],
            Convert.ToInt32(items[3]), Convert.ToDouble(items[4]));
            return order;
        }
    }
}
