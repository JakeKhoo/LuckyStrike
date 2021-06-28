# LuckyStrike
Orbital Gemini

Project Idea:

To play an arcade simulated game wirelessly from a separate computer.

Features:
Physical features:
Player’s computer which allows player to wirelessly connect to a separate computer running the game 
The separate computer is connected to the Ev3 brick through bluetooth to play the arcade game 
The arcade game is a simple car game that sends a video back to the player’s computer. The player would only have one function to stop the claw at the desired spot. 

Software features:
Game contains a log in and registration page
A top up credits page used to play the physical claw game (no real monetary top up would be used)
A record of the prizes won : big and small prize the former being of harder difficulty 
A button to play the game itself
A button to connect to the claw laptop
Only one user can be connected any one time

Design your System:
The system design is a simple green and purple scheme
The app looks like an arcade game.

Necessary Technologies:
Python
Command Socket functions 
Video streaming (Flask/OpenCV)
SQL to create the database for the app

Technical Proof of concept:
See the file 

**To run the file:**

**1. Download the schema ORBITAL Database.sql**

**2. Open Orbit.py and change the username and password below the first function defined to your individual one**

**3. Connect to SQL**

**4. Close all files and run interface.py**

Core features Developed:

The UI has been finishe using tkinter as the module.
The UI has been fully linked to the SQL data base showing how many coins the player has to play the arcade game as well as how many prizes he has won from the game.

The Lego EV3 brick has been built and the CH an intepreter has been downladed to programme the EV3 brick to receive inputs and move accordingly using a rasberry pi computer that connects to it through bluetooth. 

The game has been developed on the Lego brick although not fully tested as the physical built has not been finalised but a mock built works. However, we have yet to connect the program from the rasberry pi computer to the users computer with the lucky strike app

We used python sockets to connect a computer with the lucky strike app with the server computer with the webcam to the physical game and also the code which runs the game through an ev3 brick by bluetooth 

The client computer (with the app) just sends 2 messages to the host. When to start the game which intitiates the ev3 brick program and when to stop the car to hit the "target". (We have yet to establish this connection). The server computer then sends if the client has won and awards the player with a small or big prize

Problems:
The socket conneciton was very difficult as different website had different socket codes and connection by hostname seem not to work only connection by host ip address which had to be identified through the terminal
Initially the ev3 brick was meant to be codded in python using micropython created by the ev3dev team. Although it can be codded, inputs could not be sent to the programme or we could not find a way to send it. After awhile we read up and decided to use ch c C/C++ an intepreter on a linux os so that we can send inputs to our ev3 brick on when to stop the car to hit the "target".
the lego build for our car was also tricky as we wanted a 4 wheel drive but after realising that with four wheels the movements might have a larger error margin, preventing the car from starting of at the same position, we decided to use a 3 wheel drive where it would be easier.
To make the game more skill based, we have also decided to randomise the speed of the car so it depends if player can time the button better to be more accurate. 
