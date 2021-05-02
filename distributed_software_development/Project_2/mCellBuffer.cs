using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace Homework_2
{
    class mCellBuffer
    {
           
        public string[] data = new string[3];
        private Semaphore semaphore = new Semaphore(0, 3);

        public mCellBuffer()
        {
            for (int i = 0; i < 3; i++)
                data[i] = "";
            semaphore.Release(3);
        }
        public void Put(string order)
        {


            semaphore.WaitOne();
            lock (data)
            {
                for (int i = 0; i < 3; i++)
                {
                    if (data[i] == "")
                    {

                        data[i] = order;
                        Program.buffer_count++;
                        break;
                    }
                }

            }

        }

        public string Get()
        {
            lock (data)
            {
                for (int i = 0; i < 3; i++)
                {
                    if (data[i] != "")
                    {
                        string temp = data[i];

                        return temp;
                    }
                }
            }

            return "";

        }

        public void delete_from_Cell(string order)
        {
            for (int i = 0; i < 3; i++)
            {
                if (data[i] == order)
                {
                    semaphore.Release();
                    data[i] = "";

                    Program.buffer_count--;
                    break;
                }
            }


        }
    }
}