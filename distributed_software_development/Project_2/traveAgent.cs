using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Homework_2
{
    class traveAgent
    {
        
        string airline_name1=null;
        string airline_name2=null;
        double currentFlightPrice;
        double previousFlightPrice;
        double currentFlightPrice2;
        double previousFlightPrice2;
        int number_of_tickets;

        public traveAgent()
        {
            currentFlightPrice = 0;
            previousFlightPrice = 1000;
            currentFlightPrice2 = 0;
            previousFlightPrice2 = 1000;
            number_of_tickets = 10;
        }
        
        //Function to check if there has been a reduction in price from airline 1 or airline 2. If yes then the order will be placed
        public void order()
        {
            
            while (Program.air1.countPriceCuts<10 || Program.air2.countPriceCuts<10)
            {
                if (currentFlightPrice < previousFlightPrice || currentFlightPrice2 < previousFlightPrice2)
                {
                    //if pricecut accours for airline 1
                    if (airline_name1 == "airline1" && Program.air1.countPriceCuts < 10)
                    {
                       
                            
                        Console.WriteLine("Pacing order for   " + Thread.CurrentThread.Name + "for airline " + airline_name1 + " for number of tickets " + number_of_tickets.ToString() + " tickets");
                            
                        // creating new order object
                        OrderObject newOrder = new OrderObject(Thread.CurrentThread.Name, OrderObject.generateRandomCreditCardNo(), airline_name1, number_of_tickets, currentFlightPrice);
                            
                        // encrypting the order object
                        string encryptedObject = encoderDecoder.encrypt(newOrder);

                        // put the encrypted order in multicell buffer
                        Program.m.Put(encryptedObject);
                        Program.placed_order++;
                        airline_name1 = null;  // remove the airline name so that it doesnt places the same order again



                    }

                    //if pricecut accours for airline 1
                    else if (airline_name2 == "airline2" && Program.air2.countPriceCuts < 10)
                    {
                        
                            
                         Console.WriteLine("Placing order for  " + Thread.CurrentThread.Name + "for airline " + airline_name2 + " for  " + number_of_tickets.ToString() + " tickets");
                        // creating new order object    
                        OrderObject newOrder = new OrderObject(Thread.CurrentThread.Name, OrderObject.generateRandomCreditCardNo(), "airline2", number_of_tickets, currentFlightPrice2);

                        // encrypting the order object
                        string encryptedObject = encoderDecoder.encrypt(newOrder);

                        // put the encrypted order in multicell buffer
                        Program.m.Put(encryptedObject);
                        Program.placed_order++;
                        airline_name2 = null; // remove the airline name so that it doesnt places the same order again 
                       

                    }
                    
                }
            }
        }

        // Function to check if the order for the thread has been processed and placed in the confirmation buffer, so that it can print the confirmation
        public void travelAgencyFunc() 
        {
            

            int order_count = 0;
            do
            {
                
                Thread.Sleep(250);
                
                int hour = DateTime.Now.Hour;
                int min = DateTime.Now.Minute;
                int sec = DateTime.Now.Second;
                int totalOrder = 0;
                string cust_name = null;

               

                while (totalOrder == 0)
                {
                    Thread.Sleep(250);
                    
                         // get the total amount of order
                        (totalOrder, cust_name) =Program.confirmed_order.Get(Thread.CurrentThread.Name);
                    
                }
                order_count++;
                Console.WriteLine("The order was completed for " + cust_name+" for a total amount of  $" + totalOrder + " by " + Thread.CurrentThread.Name + ". The order was completed  at "
                  + hour + ":" + min + ":" + sec + " and time taken for processing was " + (DateTime.Now.Second - sec) + " seconds." );

            } while (order_count < 40);
            
        }

        // subscribed to the pricecut event which will update the new reduced price as per airline 1 or airline 2
        public void flightOnSale(string air_name, double newPrice) 
        {
            
            if (air_name == "airline1")
            {
                
                previousFlightPrice = currentFlightPrice;
                currentFlightPrice = newPrice;
                airline_name1 = air_name;
            }
            else if (air_name=="airline2")
            {
                
                previousFlightPrice2 = currentFlightPrice2;
                currentFlightPrice2 = newPrice;
                airline_name2 = air_name;
            }
           
        }
    }
}
