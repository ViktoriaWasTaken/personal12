using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Function to clear the screen
            static void cls()
            {
                Console.Clear();
            }

            // Function to pause the game
            static void pause()
            {
                Console.ReadKey();
            }

            // Display a title
            Console.WriteLine("game 1");

            // Ask for the player's name
            Console.Write("Tell me your name\nWhat is your name? ");
            string inputName = Console.ReadLine();

            // Welcome the player
            Console.WriteLine($"Welcome {inputName}");

            // Start the game
            Console.WriteLine("You hear a chute open you fall and hit the ground everything goes dark...");
            Console.WriteLine("...");
            Console.WriteLine("...");
            Console.WriteLine("...");
            Console.WriteLine("Open your eyes?");
            Console.WriteLine("1. Yes");
            Console.WriteLine("2. No");

            // Get the player's choice
            string inputChoice = Console.ReadLine();

            // Clear the screen
            cls();

            // Branch based on the player's choice
            string start;
            if (inputChoice == "1")
            {
                start = "You find yourself in a dark room with no defining feature besides 2 doors";
            }
            else if (inputChoice == "2")
            {
                start = "You remain unconscious";
            }
            else
            {
                start = "Invalid choice";
            }

            // Pause the game
            pause();
            // Show the situation
            Console.WriteLine(start);

            // Ask the player to choose a door
            if (start == "You find yourself in a dark room with no defining feature besides 2 doors")
        }}}