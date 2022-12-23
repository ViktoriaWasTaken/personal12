using System;
using System.Diagnostics;
using System.Linq;
using System.Threading;

namespace AdventureGame
{
    class Program
    {
        static void Main(string[] args)
        {
            // Welcome the player and prompt them for their name
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Tell me your name");
            string name = Console.ReadLine();
            ClearScreen();
            Console.WriteLine($"Welcome\n[{name}]");
            Thread.Sleep(2000);
            ClearScreen();

            // Initialize variables for the game
            int returnCount = 0;
            int progress = 1;
            int progress2 = 1;
            int branch = 0;
            int noCount = 0;
            double version = 0.3;

            while (true)
            {
                Thread.Sleep(0);
                if (progress == 1)
                {
                    // Introduce the game and present the first choice
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.WriteLine("You hear a chute open, you fall and hit the\nground. Everything goes dark...");
                    Console.WriteLine("...");
                    Console.WriteLine("...");
                    Console.WriteLine("...");
                    Console.WriteLine("Open your eyes?");
                    Console.WriteLine("1. Yes");
                    Console.WriteLine("2. No");
                    Console.WriteLine("3. Try to... ");
                    string choice = Console.ReadLine();
                    if (choice == "1" && branch == 0 && returnCount <= 1)
                    {
                        string start = $"{Console.ForegroundColor = ConsoleColor.Cyan } You find yourself in a Small dark room entirely empty with 2 doors";
                        progress = 2;
                        noCount = 0;
                        ClearScreen();
                    }
                    if (choice == "1" && branch == 0 && noCount >= 3)
                    {
                        string start = $"{ console.ForegroundColor = ConsoleColor.Cyan } You find yourself in a Small dark room entirely empty with 2 doors";
                        progress = 2;
                        ClearScreen();
                    }
                    if (choice == "1" && branch == 0 && returnCount >= 1)
                    {
                        string start = $"{ console.ForegroundColor = ConsoleColor.Cyan } You find yourself in a Small dark room entirely empty with 2 doors";
                        progress = 2;
                        ClearScreen();
                    }
                    if (choice == "2" && branch == 0 && noCount >= 3)
                    {
                        string start = $"{ console.ForegroundColor = ConsoleColor.Cyan } You find yourself in a Small dark room entirely empty with 2 doors";
                        noCount++;
                        progress = 1;
                        ClearScreen();
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("Shall you sleep forever?");
                    }
                    else if (choice == "2" && noCount <= 3)
                    {
                        progress = 1;
                        noCount++;
                        branch = 0;
                        // Return to the beginning of the loop
                        ClearScreen();
                        continue;
                    }
                    else if (choice == "3" && noCount <= 3)
                    {
                                        branch = 0;
                    progress = 1;
                    ClearScreen();
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("THERE IS NO ESCAPE");
                }
                else if (choice == "3" && noCount >= 3)
                {
                    branch = 0;
                    progress = 1;
                    ClearScreen();
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("THERE IS NO ESCAPE");
                    Console.WriteLine("Shall you sleep forever?");
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 2)
            {
                // Present the second choice
                Console.WriteLine(start);
                Console.WriteLine("Choose a door");
                Console.WriteLine("1. Wood");
                Console.WriteLine("2. Stone");
                string choice = Console.ReadLine();
                if (choice == "1")
                {
                    string choice1 = $"{ console.ForegroundColor = ConsoleColor.Cyan } You enter the wooden door and before you lays a dark misty woodland path. You hear a faint howl";
                    progress = 3;
                    branch = 1;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    string choice2 = $"{ console.ForegroundColor = ConsoleColor.Cyan } You enter the stone door and before you lays a dark damp cave. It smells of mold";
                    progress = 4;
                    branch = 2;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    progress = 2;
                    returnCount++;
                    branch = 0;
                    ClearScreen();
                    // Return to the beginning of the loop
                    continue;
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 3)
            {
                // Present the first branch of the story
                Console.WriteLine(choice1);
                Console.WriteLine("1. Press onward");
                Console.WriteLine("2. Return");
                string choice = Console.ReadLine();
                if (choice == "1")
                {
                    string choice1a = $"{ console.ForegroundColor = ConsoleColor.Cyan } You see a faint light in the distance and press on. You come to a clearing and see a old rickety cabin. Smoke rises from the chimney";
                    progress = 5;
                    branch = 3;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    returnCount++;
                    progress = 2;
                    branch = 0;
                    ClearScreen();
                    // Return to the beginning of the loop
                    continue;
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 4)
            {
                // Present the second branch of the story
                Console.WriteLine(choice2);
                Console.WriteLine("1. Press onward");
                Console.WriteLine
                                string choice = Console.ReadLine();
                if (choice == "1")
                {
                    string choice2a = $"{ console.ForegroundColor = ConsoleColor.Cyan } You see a faint light in the distance and press on. You come to a chamber with a large chest in the center. It is locked";
                    progress = 6;
                    branch = 4;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    returnCount++;
                    progress = 2;
                    branch = 0;
                    ClearScreen();
                    // Return to the beginning of the loop
                    continue;
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 5)
            {
                // Present the third branch of the story
                Console.WriteLine(choice1a);
                Console.WriteLine("1. Enter the cabin");
                Console.WriteLine("2. Return");
                string choice = Console.ReadLine();
                if (choice == "
                                    progress = 5;
                    branch = 0;
                    ClearScreen();
                    Console.WriteLine("The door is locked and won't budge");
                    Console.WriteLine("1. Return");
                    Console.WriteLine("2. Knock on the door");
                    string choice = Console.ReadLine();
                    if (choice == "1")
                    {
                        returnCount++;
                        progress = 2;
                        branch = 0;
                        ClearScreen();
                        // Return to the beginning of the loop
                        continue;
                    }
                    else if (choice == "2")
                    {
                        string choice5a = $"{ console.ForegroundColor = ConsoleColor.Cyan } An old man opens the door and invites you in. He offers you a warm meal and a bed to sleep in";
                        progress = 7;
                        branch = 5;
                        ClearScreen();
                    }
                    else
                    {
                        ClearScreen();
                        // End the loop if the player enters an invalid choice
                        continue;
                    }
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 6)
            {
                // Present the fourth branch of the story
                Console.WriteLine(choice2a);
                Console.WriteLine("1. Try to open the chest");
                Console.WriteLine("2. Return");
                string choice = Console.ReadLine();
                if (choice == "1")
                {
                    string choice2b = $"{ console.ForegroundColor = ConsoleColor.Cyan } The chest opens and inside you find a sword and a note that reads 'You are the chosen one. Use this sword to defeat the dragon and bring peace to the land'";
                    progress = 8;
                    branch = 6;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    returnCount++;
                    progress = 2;
                    branch = 0;
                    ClearScreen();
                    // Return to the beginning of the loop
                    continue;
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 7)
            {
                // Present the fifth branch of the story
                Console.WriteLine(choice5a);
                Console.WriteLine("1. Stay the night");
                Console.WriteLine("2. Leave");
                string choice = Console.ReadLine();
                if (choice == "1")
                {
                    string choice5b = $"{ console.ForegroundColor = ConsoleColor.Cyan } You wake up the next morning to find the old man gone and a key on the table next to you";
                    progress = 9;
                    branch = 7;
                    ClearScreen();
                }
                else if (choice == "2")
                {
                    returnCount++;
                    progress = 2;
                    branch = 0;
                    ClearScreen();
                    // Return to the beginning of the loop
                    continue;
                }
                else
                {
                    ClearScreen();
                    // End the loop if the player enters an invalid choice
                    continue;
                }
            }
            else if (progress == 8)
            {
            }
               


