# Chapters-Projects

<b>Chapter I</b>

Starting a program (car.py):

A program can be simply launched in the terminal by running a python command and providing the name of the file:

python car.py

Function: 

Program will ask for additional details in order to create an instance of a Car object. If provided arguments are valid, the relevant message will be printed to the screen and Car parameters will be displayed to the user. If provided arguments are invalid, the relevant error message will be displayed.

<b>Chapter II</b>

The program is using Invoke module, therefore instalation may be required. The easiest to do it is with pip:

$ pip install invoke

Starting a program (tasks.py) :

To run the program, task managing script needs to be created as tasks.py. All the commands need to be passed to the terminal as follows:

invoke function name --argument1 --argument2 etc

Functions and possible arguments:

- function: add; arguments: --name, --deadline, --description (all default)
- function: update; arguments: hash_value (default), --name, --deadline, --description (optional)
- function: remove; arguments: hash_value (default)
- function: present; arguments: --all, --deadline (optional)

<b> Chapter III</b>

Starting the program (number.py) :

The program can be launched by simply running the python command along with the name of the file in the terminal:

python number.py

Program calculates all the numbers meeting the provided criteria and then asks if the user wants to display them to the screen.




