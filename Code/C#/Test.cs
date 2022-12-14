using System;

namespace TextGame
{
    class Program
    {
        static void Main(string[] args)
        {
            // Set the initial health of the player
            int health = 100;

            // Set the initial location of the player
            string location = "room";

            // Print a welcome message
            Console.WriteLine("Welcome to the game! You are in a dark room. Your health is 100.");

            // Start the game loop
            while (true)
            {
                // Prompt the player for input
                Console.WriteLine("What would you like to do?");
                string input = Console.ReadLine();

                // Handle the player's input
                if (input == "quit")
                {
                    // If the player wants to quit, break out of the game loop
                    break;
                }
                else if (input == "look")
                {
                    // If the player wants to look around, print the current location
                    Console.WriteLine("You are in a " + location);
                }
                else if (input == "health")
                {
                    // If the player wants to check their health, print their current health
                    Console.WriteLine("Your health is " + health);
                }
                else
                {
                    // If the player enters an unrecognized command, print an error message
                    Console.WriteLine("I'm sorry, I didn't understand that.");
                }
            }

            // Print a goodbye message when the game ends
            Console.WriteLine("Thanks for playing!");
        }
    }
}