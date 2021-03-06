# icodeAI Challange [![Build Status](https://travis-ci.org/antonnifo/icodeAI_sandbox.svg?branch=develop)](https://travis-ci.org/antonnifo/icodeAI_sandbox) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Maintainability](https://api.codeclimate.com/v1/badges/787afbed9ac0111ba9cc/maintainability)](https://codeclimate.com/github/antonnifo/icodeAI_sandbox/maintainability) 
#### Getting Started 
 > git clone https://github.com/antonnifo/icodeAI_sandbox  
 > create a virtual environment,activate it & install the dependencies  
 ```
 virtualenv venv -p python3
 source venv/bin/activate
 pip3 install -r requirements.txt
 python3 dice/dice_simulator.py 
 python3 password/pass_checker.py
 pytest
 ```
 
#### Dice Rolling Simulator 

When the program runs, it will randomly choose a number between 1 and 6.
(Or whatever other integer you prefer — the number of sides on the die is up to you.) 
The program will print what that number is. It should then ask you if you’d like to roll again.  
#### Password checker 
The program checks the validity of password input by a given user. 
The following are the criteria for checking the password: 
```
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
No white spaces 
``` 
#### Testing the scripts  
Tests are to be run with pytest or py.test on the root folder 
#### Running the code 
 [repls...online python compiler/editor](https://repl.it/@antonnifo/icodeAIsandbox-1 "Run the code")
