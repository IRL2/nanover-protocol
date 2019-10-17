﻿using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Timers;
using Newtonsoft.Json;
using Timer = System.Timers.Timer;

namespace Essd
{
    
    // https://stackoverflow.com/questions/19404199/how-to-to-make-udpclient-receiveasync-cancelable
    public static class AsyncExtensions
    {
        /// <summary>
        /// Enables a task to be cancellable.
        /// </summary>
        /// <param name="task">Task that usually cannot be canceled.</param>
        /// <param name="cancellationToken">Cancellation token to use for cancellation.</param>
        /// <typeparam name="T">Task result type.</typeparam>
        /// <returns>Task</returns>
        /// <exception cref="OperationCanceledException">If the task is cancelled before completion.</exception>
        public static async Task<T> WithCancellation<T>( this Task<T> task, CancellationToken cancellationToken )
        {
            var tcs = new TaskCompletionSource<bool>();
            using( cancellationToken.Register( s => ( (TaskCompletionSource<bool>)s ).TrySetResult( true ), tcs ) )
            {
                if( task != await Task.WhenAny( task, tcs.Task ) )
                {
                    throw new OperationCanceledException( cancellationToken );
                }
            }

            return task.Result;
        }
    }
    
    /// <summary>
    /// Implementation of an Extremely Simple Service Discovery (ESSD) client. 
    /// </summary>
    public class Client
    {
        /// <summary>
        /// Default port upon which ESSD clients listen for services.
        /// </summary>
        public const int DefaultListenPort = 54545;


        /// <summary>
        /// Whether this client is currently searching for services.
        /// </summary>
        public bool Searching => searching;

        /// <summary>
        /// Event triggered when a service is found.
        /// </summary>
        public event EventHandler<ServiceHub> ServiceFound; 
        
        private UdpClient udpClient;

        private CancellationTokenSource cancellationTokenSource = new CancellationTokenSource();
        private bool searching;
        private Task searchTask;

        /// <summary>
        /// Initialises an ESSD client.
        /// </summary>
        /// <param name="listenPort">Port at which to listen for services.</param>
        public Client(int listenPort=DefaultListenPort)
        {
            udpClient = new UdpClient();
    
            udpClient.Client.Bind(new IPEndPoint(IPAddress.Any, listenPort));
        }

        public Task StartSearch()
        {
            if (searching)
                throw new InvalidOperationException("Already searching!");
            searchTask = SearchForServicesAsync(cancellationTokenSource.Token);
            return searchTask;
        }

        private async Task SearchForServicesAsync(CancellationToken token)
        {
            searching = true;
            while (!token.IsCancellationRequested)
            {
                UdpReceiveResult message;
                try
                {
                    message = await udpClient.ReceiveAsync().WithCancellation(token);
                }
                catch (OperationCanceledException)
                {
                    break;
                }
                
                ServiceHub service;
                try
                {
                    service = DecodeServiceHub(message.Buffer);
                }
                catch (ArgumentException e)
                {
                    Console.WriteLine($"ESSD: Exception passing service definition: {e.Message}");
                    continue;
                }

                ServiceFound?.Invoke(this, service);

            }

            searching = false;
        }

        public async Task StopSearch()
        {
            if(!searching)
                throw new InvalidOperationException("Attempted to stop a non-existent search for services");
            cancellationTokenSource.Cancel();
            await searchTask;
        }
        
        /// <summary>
        /// Searches for services for the given duration, blocking.
        /// </summary>
        /// <param name="duration">Duration to search for, in milliseconds.</param>
        /// <returns>Collection of unique services found during search.</returns>
        /// <remarks>
        /// There is no guarantee that services found during the search will still
        /// be up after the search ends.
        /// </remarks>
        public ICollection<ServiceHub> SearchForServices(int duration=3000)
        {
            if (Searching)
                throw new InvalidOperationException(
                    "Cannot start a blocking search while running another search in the background");
            
            HashSet<ServiceHub> servicesFound = new HashSet<ServiceHub>();

            var from = new IPEndPoint(0, 0);
            
            var timer = new Timer(duration);
            udpClient.Client.ReceiveTimeout = duration;
            timer.Elapsed += OnTimerElapsed;
            bool timerElapsed = false;
            timer.Start();
            
            while(!timerElapsed)
            {

                var (timedOut, messageBytes) = WaitForMessage(ref from);
                if (timedOut)
                    break;
                
                ServiceHub service;
                try
                {
                    service = DecodeServiceHub(messageBytes);
                }
                catch (ArgumentException e)
                {
                    Console.WriteLine($"ESSD: Exception passing service definition: {e.Message}");
                    continue;
                }

                servicesFound.Add(service);
            }

            return servicesFound;

            void OnTimerElapsed(object sender, ElapsedEventArgs e)
            {
                timerElapsed = true;
            }
            
        }


        private ServiceHub DecodeServiceHub(byte[] messageBytes)
        {
            var message = DecodeMessage(messageBytes);
            ServiceHub service;
            try
            {
                service = new ServiceHub(message);
            }
            catch (JsonException e)
            {
                throw new ArgumentException("Invalid JSON string encountered.");
            }
            
            return service;
        }
        private (bool, byte[]) WaitForMessage(ref IPEndPoint from)
        {
            byte[] messageBytes;
            try
            {
                messageBytes = udpClient.Receive(ref from);
            }
            catch (SocketException e)
            {
                if(e.SocketErrorCode == SocketError.TimedOut)
                    return (true, null);
                throw;
            }

            return (false, messageBytes);
        }
        private string DecodeMessage(byte[] messageBytes)
        {
            try
            {
                var message = Encoding.UTF8.GetString(messageBytes);
                return message;
            }
            catch (ArgumentException)
            {
                throw new ArgumentException("ESSD: Received invalid message, not a valid UTF8 string.");
            }
            
        }


    }
}