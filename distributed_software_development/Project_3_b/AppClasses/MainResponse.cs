using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace homework3_b.AppClasses
{
    public class MainResponse
    {
        public string version { get; set; }
        public List<object> warnings { get; set; }
        public List<object> errors { get; set; }
        public Metadata metadata { get; set; }
        public Inputs inputs { get; set; }
        public Outputs outputs { get; set; }
    }
}