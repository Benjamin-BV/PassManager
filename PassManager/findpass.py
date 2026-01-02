#Find a password in the passwords.txt file by service name, if service name found, return password
def findservice(service):
    #Iterate through each line until service name is found in 'Passwords.txt' (CURRENTLY DEFAULT, CAN ALLOW USER TO CUSTOMIZE PATH)
    pwfile = open("Passwords.txt", 'r'); #Allow reading of file, should not be allowed to edit it
    global pw;
    global service_real;
    pw = None;
    for line in pwfile:
        if(line.strip('\n').lower() == service.lower()):
            pw = next(pwfile);
            service_real = line.strip().strip('\n'); #To get the real inputted service name
            break;
    pwfile.close();   
    if(pw == None):
        print("Password not found, ensure filepath is correct, and service name is correct");
        return -1;
    return 0

def main():
    service = input("Which service do you want to find the password of?: ");
    found = findservice(service);

    if(found == 0):
        print("Password for service {} is: {}".format(service_real, pw.strip('pass: ')));1

    return 0;

main();