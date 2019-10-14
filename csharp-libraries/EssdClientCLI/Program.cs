﻿using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using Essd;

namespace EssdClientCLI
{
    
    class Program
    {
        static void Main(string[] args)
        {

            CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
            var task = Task.Run(() => RunSearches(), cancellationTokenSource.Token);
            Console.WriteLine("Press any key to exit.");
            while (!Console.KeyAvailable)
            {
                if (task.Exception != null)
                    throw task.Exception;
            }
            cancellationTokenSource.Cancel();
        }

        private static void RunSearches()
        {
            Client essdClient = new Client();
            while (true)
            {
                var services = essdClient.SearchForServices();
                Console.WriteLine($"Number of services found: {services.Count}");
                foreach (var service in services)
                {
                    Console.WriteLine($"    - {service.Name}:{service.Address}");
                }
            }
            
        }
    }
}