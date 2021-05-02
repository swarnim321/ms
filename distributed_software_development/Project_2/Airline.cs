using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;


namespace Homework_2
{
    class Airline
    {
        static Random rng = new Random();
        public static event priceCutEvent priceCut;    // creating an event
        private  double ticketPrice = 900;  // initial ticket price    
        public   Int32 countPriceCuts = 0;
        public  Int32 total_number_order = 0;
        public Int32 Flag = 0;
        public Int32 i = 0;
        public Int32 p = 0;
        public Int32 abort = 0;
        int[] price_table = new int[] { 250, 200, 150,100, 450 ,500, 400,350,300,325,300,250,200,150 };// price table to get the pricecut for airlines
        private OrderProcessing op = new OrderProcessing();
        
    

       // If the new price is less than previous price for the airline, price cut event is called
        public  void changePrice(string airlineName, double newPrice)
        {
            if (newPrice < ticketPrice) 
            { 
                if (priceCut != null)
                {  
                    Console.WriteLine("pricecut occured for " + airlineName + " with new price " + newPrice);
                    priceCut(airlineName, newPrice); //call the pricecut event
                    countPriceCuts++; // increase number of price cut count
                }

            }
            ticketPrice = newPrice;
        }

       //Function to get order fom buffer and process the order
       // and to call the changePrice function based of new price
        public void AirlineFunc(string name)
        {
            while (true)

            {
                if (Program.buffer_count==0 && Flag== 1 ) // exit the loop
                {
                   
                    break;
                }
                Thread.Sleep(1000);

                 string orderencoded = "";
                 Console.WriteLine("number of price cuts:" + countPriceCuts);
                 


                 orderencoded = Program.m.Get(); // get the order from buffer


                 if (orderencoded != "")
                 {

                    Flag = 1;
                    OrderObject orderDecoded = encoderDecoder.decrypt(orderencoded); // decrypt the order

                     //Decide the price based on the orders
                     if (name == orderDecoded.getReceiverID()) // if the order is for this airline thread
                     {
                         
                         Console.WriteLine("Processing the order for " + orderDecoded.getReceiverID()+" of amount " + orderDecoded.getAmount() +"for " + orderDecoded.getSenderID());
                         Thread orderProc = new Thread(new ThreadStart(() => op.orderFunc(orderDecoded))); //  createthread  and start the processing of order
                         orderProc.Start();
                         Program.m.delete_from_Cell(encoderDecoder.encrypt(orderDecoded)); // delete the order form multicell buffer
                         total_number_order++;
                         
                     }
                 }

                if (i < 14) // iterate through price table to check for price cuts
                {
                    p = price_table[i];
                    i++;
                }
                if (countPriceCuts < 10) // if pricecut less than 10 then call the changePrice function
                {
                    changePrice(name, p);
                }
                
                
            }

            //Print the summary for each airline thread
            Console.WriteLine(" " );
            Console.WriteLine("SUMMARY FOR AIRLINE: " + Thread.CurrentThread.Name);
            Console.WriteLine("Total Price cut events " + countPriceCuts.ToString());
            Console.WriteLine("Total orders from travel agents for this airline " + total_number_order.ToString());
            Console.WriteLine("Successfull orders for this airline "+ (total_number_order - op.getRejected_order()).ToString());
            Console.WriteLine("Total Rejected orders for this airline "+ op.getRejected_order().ToString());
            Console.WriteLine(" ");

            // Terminate the thread of processing is done with required amount of pricecut
            abort = 1;
            Thread.CurrentThread.Abort();

        }
    }
}
