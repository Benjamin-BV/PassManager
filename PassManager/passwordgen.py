# General security specifications for a password require: 
# At least 1 Uppercase
# At least 1 special character
# At least 1 Number
# At least 1 lowercase
# Minimum length of 8

#Minimum specs ex.: Bq8#ozLv
#High specs ex.: Io0w9eor;f'!@jaidsofzxcmMMDASIF>?193kdsfi

from random import *
import random

charAmnt = 0;
def generate(char):
    #Setting flags to be global so changes in function apply to whole namespace, and are not erased after the fact
    global lowflag;
    global upflag; 
    global numflag;
    global specflag;
    
   
    #Generate a lowercase:
    if(char == 0):
        lowflag = True;
        return chr(SystemRandom().randint(97,122));

    #Generate an uppercase:
    if(char == 1):
        upflag = True;
        return chr(SystemRandom().randint(65,90));

    #Generate a number:
    if(char == 2):
        numflag = True;
        return str(SystemRandom().randint(0,9));

    #Generate a special char:     
    #Also should consider: [58,64], 
    #use an if conditional and set some RNG seeding for sysRandom 
    #so if RNG > .33, be this, if RNG > .66, be that, else be other or something similar to this 
    #consider invalid values and use those as selectors is another possibility

    if(char == 3):

        specflag = True;
        rng = random.uniform(0,1);#Need to figure out how to make this work properly
        if(rng > 0.5):
            return chr(SystemRandom().randint(58,64));
        
        else:
            return chr(SystemRandom().randint(33, 47));

def askPass():
    passReq = input("What strength do you need your password to be?(HIGH - 32 char, MED - 16 char, LOW - 8 char):\n");
    if(passReq.lower() == "high"):
        pwd = genPass(32);
    elif(passReq.lower() == "med" or passReq.lower() == "medium"):
        pwd = genPass(16)
    elif(passReq.lower() == "low"):
        pwd = genPass(8);
    else:
        print("Invalid input, please input either: HIGH, MED, LOW\n");
        askPass();
    return pwd;
#Setting flag values
lowflag = False; upflag = False; numflag = False; specflag = False;
#Our flags that we use to determine when we have a character, making sure that we meet our char requirements
flags = [lowflag, upflag, numflag, specflag];
#Our password list, to be turned into a string 
pwd = [];
global passwrd;

def genPass(chars):
    for i in range(0, chars):
        #Generate a random character, making sure we follow our specifications, and that we make sure that we do not miss a required target
            if(not all(flags) and i + (4 - sum(flags)) >= charAmnt):
                pwd.append(generate(randint(0,3)));
    passwrd = ''.join(pwd) + '\n';
    return passwrd;   


#Function that gets service password is for
def askService():
    service = input("Which service are you generating a password for?:\n");
    return service;



def main():
    #Add a file "Passwords.txt to program to store passwords locally"
    file = open("Passwords.txt", "a");#Eventually change to a user-designated file path
    service = askService(); #Store service name
    pw = askPass();
    file.write(service + '\n');
    file.write("pass: " + pw + '\n'); #Write the password to file, with service name above
    file.close();
main();