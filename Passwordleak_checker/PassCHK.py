import argparse
import hashlib
import os
import requests
import sys

# text color
CLR_RED = '\033[31m'
CLR_GREEN = '\033[32m'
CLR_END = '\033[0m'

def send_request(text_password_list, hash_password_list):
    flag = ""

    if len(hash_password_list) == 1:
        url = "https://api.pwnedpasswords.com/range/" + single_hash_password[0:5]
        # Convert response valiable from str to list
        response = requests.get(url).text.splitlines()

        for hashes in response:
            if (single_hash_password[5:40] in hashes):
                flag = "True"
                break
            else:
                flag = "False"
        if flag == "True":
            print("password: " + password+"\n" + "result: " + CLR_RED + "Pwned!!" + CLR_END)
        else:
            print("password: " + password+"\n" + "result: " + CLR_GREEN + "No pwned!!" + CLR_END)  

    else:
        c = 0
        for file_hashed_passwords in hash_password_list:
            url = "https://api.pwnedpasswords.com/range/" + file_hashed_passwords[0:5]
            response = requests.get(url).text.splitlines()
            
            for hashes in response:
                if (file_hashed_passwords[5:40] in hashes):
                    flag = "True"
                    break
                else:
                    flag = "False"
            
            if flag == "True":
                print("password: " + text_password_list[c]+"\n" + "result: " + CLR_RED + "Pwned!!" + CLR_END)
            else:
                print("password: " + text_password_list[c]+"\n" + "result: " + CLR_GREEN + "No pwned!!" + CLR_END)  
            c+=1

if __name__ == "__main__":

    #help menu
    parse = argparse.ArgumentParser(
    usage="\nPassCHK.py -h" + "\nPassCHK.py -p <Password>\n" + "PassCHK.py -f <PasswordList>\n")
    parse.add_argument('-p', '-password', help='Specify the password')
    parse.add_argument('-f', '-file', help='Specify the password file')
    args = parse.parse_args()

    # password option
    if sys.argv[1] == '-p' or sys.argv[1] == '-password':
        password = sys.argv[2]
        encode = password.encode("utf-8")
        single_hash_password = hashlib.sha1(encode).hexdigest().upper()
        send_request("", [single_hash_password])

    # file option
    elif sys.argv[1] == '-f' or sys.argv[1] == '-file' and os.path.isfile(sys.argv[2])==True:
        text_password_list = []
        hash_password_list = []
        with open(sys.argv[2]) as file:
            for line in file:
                password = line.replace("\n", "")
                #This code is used to display the plain text password.
                text_password_list.append(password)
                encode = password.encode("utf-8")
                tmp_hash = hashlib.sha1(encode).hexdigest().upper()
                hash_password_list.append(tmp_hash)
        send_request(text_password_list, hash_password_list)
