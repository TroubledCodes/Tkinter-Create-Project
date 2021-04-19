import tkinter as tk  # GUI library, preinstalled with python

# variable definition

i = 0
e = 0
g = 0
been_called = False

# list definition
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# the alphabet used for encryption and decryption

verifiedusers = ['qrergy', 'vrpherhy', 'dxvhu']  # preencrypted username and password for maximum security
verifiedpass = ['zlqhydorq', 'hofrph12345', 'odvwsdvv']

# Getting a window
window = tk.Tk(className=' External Login Page')
window.geometry('300x250')

label_ = tk.Label(text="Input Username and Password here")  # making that text at the top of the screen
label_.pack()
_label = tk.Label(text=' ')

password_input = tk.Entry()  # the input places and stuff
username_input = tk.Entry()
username_input.pack()
password_input.pack()

called_func = 0

# Function definition
def validuser(unverifieduser, unverifiedpass):  # the function to verify the login
    for g in range(0, len(verifiedusers)):
        what = verifiedusers[g]
        what2 = verifiedpass[g]
        if unverifieduser == what and unverifiedpass == what2:
            confirmation = True
        else:
            confirmation = False
        return confirmation


def append_information(label, has_been_called):
    called = has_been_called
    passw = encrypt(password_input.get())  # taking the information
    user = encrypt(username_input.get())
    nice = validuser(user, passw) # validating the user
    if called == True:
        label.pack_forget()
    if nice is not True:
        label = tk.Label(text="Error - Incorrect Credentials")
        label.pack()
    else:
        label = tk.Label(text="Successfully Logged In!")
        label.pack()
    called = True
    has_been_called = called


def encrypt(toBeEncrypt):  # simple hash encryption
    hashed = 0
    stringToBeEncrypt = str(toBeEncrypt)
    listToBeEncrypt = list(stringToBeEncrypt)
    for i in range(len(stringToBeEncrypt)):
        letter = listToBeEncrypt[i]
        for e in range(36):
            if letter == alphabet[e]:
                hashed += e
                print(hashed)
            hashed += 1
    return hashed


# all of the juicy Tkinter stuff

input_confirmed = tk.Button(text="Log On", width=5, height=2, command=lambda: append_information(_label, been_called))  # *button*
input_confirmed.pack()
register_initiate = tk.Button(text='Register')


window.mainloop()  # Loop the window to exist
called_func = 0