# L3T8 Compulsory Task 1.

## Description:

This repository contains the files for Level 3, Task 8, Compulsory 
Task 1 with instructions for running in a Docker Container. The 
purpose of this task is to highlight Python coding ability and all
methods and techniques that implies including object oriented programming, 
defensive programming, exception handling, reading from and writing to 
external data sources, and function definition.

It also demonstrates familiarity with containerisation such as Docker. 
I could just drop the code in this repo and leave the visitor to 
clone it into their system and run manually in VSC, however this 
would require selecting an appropriate python interpreter whereas 
if run via Docker Desktop, all this is taken care of via the Docker 
File.

## Table of Contents:

### 1 - Installation
### 2 - Usage
### 3 - Credits

## 1 - Installation:

This requires Docker Desktop be installed if not already.

In an appropriate location/folder create a clone of this repository by 
running the following command in VSC or command line (remember to open 
the folder in VSC, or open terminal within the folder). I reccomend 
command line opened in the appropriate folder as it demonstrates the 
app running indepedent of VSC.

#### "git clone https://github.com/chatsim79/L3T8CS1-Containerised"

once the repository is cloned, cd into the Compulsory Task 1 folder:

"cd L3T8CS1-Containerised"

"cd Compulsory Task 1"

run the following command, providing an approriate app name:

"docker build -t [app name] ./"

The Build process will occur automatically.

## 2 - Usage:

to use the app, run the following command.

"docker run -it [app name]"

I recommend one of the first selections when using the app should be
"view current stock". This will produce a table of stock model names
and SKU codes, these can they be used in conjunction with other 
elements of the menu which will request a stock name or SKU code to 
perform actions.

## 3 - Credits: 

Me :) Also thanks to John and Njabulo, who always provide excellent
assistance.
