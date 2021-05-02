using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Homework_2
{
    class OrderObject
    {
        private string senderID; //Travel agents id
        private int credit_card_No;      // an integer representing a credit card number
        private string receiverID; // Airline id
        private int amount;     // number of tickets
        private double unitPrice;  // new price of each tickets
        static Random rng = new Random(); // to generate  numbers for credit card 
        public OrderObject(string SendID, int cardNo, string ReceiveID, int amt, double unitP)
        {
            senderID = SendID;
            credit_card_No = cardNo;
            receiverID = ReceiveID;
            amount = amt;
            unitPrice = unitP;
        }

        // Function to generate random credit card number
        public static int generateRandomCreditCardNo()
        {
            return rng.Next(5000, 7000);
        }

        //Function to get travel agents name
        public string getSenderID()
        {
            return senderID;
        }

        //Function to get the airlines name
        public string getReceiverID()
        {
            return receiverID;
        }

       //Function to get the credit card number
        public int getCardNum()
        {
            return credit_card_No;
        }

        //Function to get the price of one ticket
        public double getUnitPrice()
        {
            return unitPrice;
        }

        //Function to get the total number of tickets
        public int getAmount()
        {
            return amount;
        }

  
    }
}
