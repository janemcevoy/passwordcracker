import tkinter
from tkinter import *
import hashlib
import itertools
import string
import time
from urllib.request import urlopen
import threading

root = Tk()
root.title("Password Cracker")
root.geometry("650x400")
root.config(background="#B7365F")

heading = Label(root, text = "Password Cracker", font = ("Cascadia code light", 20, "bold"), bg="#B7365F", fg="#323963")
heading.pack(pady=(50,0))
intro = Label(root, text = "Welcome to our Password Cracker! \n \n It can work out passwords made up of letters (upper and lower case), \n numbers and symbols that are < 10 characters long. \n \n To try, please enter a password: ", font = ("Cascadia code light", 15), bg="#B7365F", fg="#323963")
intro.pack(pady=(20,0))
enter_text = Entry(root, justify="center", width=30, font=("Cascadia code light", 20, "bold"), bg="white", border=2)
enter_text.pack(pady=10)
enter_text.focus()


def password_cracker():
    try:
        def readwordlist(url): ## reads the url of passwords
            try:
                wordlistfile = urlopen(url).read()
            except Exception as e:
                print("Hey there was some error while reading the wordlist, error:", e)
                exit()
            return wordlistfile


        def hash(password): ## hash of password?
            result = hashlib.sha1(password.encode())
            return result.hexdigest()

        url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
        wordlist = readwordlist(url).decode('UTF-8') #converts bytes to string object
        guesspasswordlist = wordlist.split('\n') #this variable is the list of passwords from the url split by a paragraph

        def bruteforce(guesspasswordlist, actual_password_hash):
            for guess_password in guesspasswordlist:
                if hash(guess_password) == actual_password_hash:
                    shpiel = "Your password is '{}'. \n Please change this, it was on our common password list!".format(guess_password)
                    cracker.config(text=shpiel)
                    quit()
                                
        actual_password = enter_text.get()
        actual_password_hash = hash(actual_password)

        bruteforce(guesspasswordlist, actual_password_hash)

        def guess_password(real):
            chars = string.printable
            attempts = 0
            for password_length in range(1, 9):
                for guess in itertools.product(chars, repeat=password_length):
                    attempts += 1
                    guess = ''.join(guess)
                    if guess == real:
                        shpiel = "Your password is {}. \n It was not on our word list but we found it in {} \n random guesses.".format(guess, attempts)
                        cracker.config(text=shpiel)
                        
        print(guess_password(actual_password))

        time.sleep(180)
    except:
        print("Password secure, took too long to crack")

def start_password_cracker():
    threading.Thread(target=password_cracker).start()

Button=Button(root, text="Enter", font=("Cascadia code light", 20, "bold"), fg="black", bg = "white", command=start_password_cracker)
Button.pack()

cracker = Label(root, font=("Cascadia code light", 20), bg="#B7365F", fg="#323963")
cracker.place(x=200, y=400)

root.mainloop()
