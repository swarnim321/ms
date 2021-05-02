using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
  
namespace Homework_2
{
    // Developed in Visual Studio 2019
    public delegate void priceCutEvent(string airlineName, double newPrice); // creating a delegate
       
    class Program
    {
        public static AutoResetEvent orderCompleted = new AutoResetEvent(false); 
        public static mCellBuffer m = new mCellBuffer();  //instantiating multicell buffer which will have the orders placed by travel agent
        public static process_order_buffer confirmed_order = new process_order_buffer();    // instantiating processed order buffer where the orders will be placed after it is processed by the airline    
        public static Int32 placed_order = 0; 
        public static Int32 processed_order = 0;
        public static Int32 buffer_count = 0;
        public static Airline air1 = new Airline();  // instantiating airline 1 object      
        public static Airline air2 = new Airline(); //instantiating airline 2 thread
        static void Main(string[] args)
        {

            try
            {
                Thread airline1 = new Thread(new ThreadStart(() => Program.air1.AirlineFunc("airline1"))); // creating thread for airline 1
                Thread airline2 = new Thread(new ThreadStart(() => Program.air2.AirlineFunc("airline2"))); // creating thread for airline 2

                airline1.Name = "airline 1";
                airline2.Name = "airline 2";

                // starting airline 1 and 2 thread
                airline2.Start();
                airline1.Start();

               
                //creating 5 objects for 5 travel agents
                traveAgent travel = new traveAgent();
                traveAgent travel2 = new traveAgent();
                traveAgent travel3 = new traveAgent();
                traveAgent travel4 = new traveAgent();
                traveAgent travel5 = new traveAgent();

                // subscribing pricecut events of the airline to the 5 travel agents
                Airline.priceCut += new priceCutEvent(travel.flightOnSale);
                Airline.priceCut += new priceCutEvent(travel2.flightOnSale);
                Airline.priceCut += new priceCutEvent(travel3.flightOnSale);
                Airline.priceCut += new priceCutEvent(travel4.flightOnSale);
                Airline.priceCut += new priceCutEvent(travel5.flightOnSale);

                //creating array which will hold the threads for travel agents
                Thread[] travelAgent1 = new Thread[5];
                Thread[] travelAgent2 = new Thread[5];

                // starting threads for travel agents which will check for the confirmation of order from the confirmation buffer
                travelAgent1[0] = new Thread(new ThreadStart(travel.travelAgencyFunc));
                travelAgent1[0].Name = "travel agency " + (1).ToString();
                travelAgent1[0].Start();

                travelAgent1[1] = new Thread(new ThreadStart(travel2.travelAgencyFunc));
                travelAgent1[1].Name = "travel agency " + (2).ToString();
                travelAgent1[1].Start();

                travelAgent1[2] = new Thread(new ThreadStart(travel3.travelAgencyFunc));
                travelAgent1[2].Name = "travel agency " + (3).ToString();
                travelAgent1[2].Start();

                travelAgent1[3] = new Thread(new ThreadStart(travel4.travelAgencyFunc));
                travelAgent1[3].Name = "travel agency " + (4).ToString();
                travelAgent1[3].Start();

                travelAgent1[4] = new Thread(new ThreadStart(travel5.travelAgencyFunc));
                travelAgent1[4].Name = "travel agency " + (5).ToString();
                travelAgent1[4].Start();


                // creating threads for travel agents which will check for the lastest pricecuts from the airline and place order for the same
                travelAgent2[0] = new Thread(new ThreadStart(travel.order));
                travelAgent2[0].Name = "travel agency " + (1).ToString();
                travelAgent2[0].Start();

                travelAgent2[1] = new Thread(new ThreadStart(travel2.order));
                travelAgent2[1].Name = "travel agency " + (2).ToString();
                travelAgent2[1].Start();

                travelAgent2[2] = new Thread(new ThreadStart(travel3.order));
                travelAgent2[2].Name = "travel agency " + (3).ToString();
                travelAgent2[2].Start();

                travelAgent2[3] = new Thread(new ThreadStart(travel4.order));
                travelAgent2[3].Name = "travel agency " + (4).ToString();
                travelAgent2[3].Start();

                travelAgent2[4] = new Thread(new ThreadStart(travel5.order));
                travelAgent2[4].Name = "travel agency " + (5).ToString();
                travelAgent2[4].Start();


                // check if airline thread is alive. If both the airline threads are terminated then the travel agent threads will also be temrinated
                while (true)
                {
                    Thread.Sleep(500);
                    
                    if (airline1.IsAlive == false && airline2.IsAlive == false)
                    {
                        Console.WriteLine(" Airline threads terminated , terminating Travel agent thread ");

                        for (int i = 0; i < 5; i++)

                        {


                            travelAgent1[i].Abort();
                            travelAgent2[i].Abort();

                            

                        }
                        break;
                    }
                }
                Console.WriteLine("---------Done with all the threads---------");
            }
            catch(Exception e)
            {
                Console.WriteLine("Error in execution ; try again; error:" + e);
            }
        }
    }
}
