# This script heavily relies on bash to function.
# you might want to tweak some code to make some
# features work !!

import wikipedia
import os
import googlesearch

# main menu
def menu():

    print("Welcome!")
    cho1 = input("What do you need help with?\n1) Calculator\n2) Wikipedia\n3) Bash\n4) Google:: ")

    if cho1 == "1":
        calculator()

    if cho1 == "2":
        wiki()

    if cho1 == "3":
        bash()

    if cho1 == "4":
        google()
# end of main menu


# calculator function
def calculator():
    num1 = float(int(input("-")))
    op1 = input("(+) (-) (/) (x): ")
    num2 = float(int(input("-")))

    if op1 == "+":
        print(num1 + num2)

    elif op1 == "-":
        print(num1 - num2)

    elif op1 == "/":
        print(num1 / num2)

    elif op1 == "x":
        print(num1 * num2)

    else:
        print("Invalid operator.")
    back_menu1()

# end of calculator

# wikipedia function

def wiki():

    # taking options
    cho_wiki = input("1) Search something up\n2) Exit\n:: ").lower()
    if cho_wiki == "1":

        # search stuff up
        wiki_search = input("Enter what you want to search up: ")
        print(wikipedia.search(wiki_search))

        wiki_search1 = input("Choose one from the list: ")
        print(wikipedia.summary(wiki_search))
        full = input("Full search (Y/N): ").lower()

    else:
        menu()

    if full == "y":
        print(wikipedia.page(wiki_search1).content)

        # end

    # calling the back menu (of wiki function)
    back_menu0()
# end if wikipedia function

bash1 = ""
# this will need some tweaking since i made it for my own system.
def bash():
    bash_menu = input("1) Play Music\n2) Open PyCharm\n 3) Activate Cameras\n:")

    if bash_menu == "1":
        os.system("parole ~/Desktop/Music/") # parole is my media player. you could try vlc.

    if bash_menu == "2":
        os.system("bash ~/Desktop/pycharm/bin/pycharm.sh")

    if bash_menu == "3":
        os.system("parole ~/Desktop/RTSP/playlist.m3u") # Security Cameras i set up using 2 broken phones.

def google():
    query = input("Surf the web!\n::")

    for j in googlesearch.search(query, tld="com", num=5, start=0, pause=2.0):
        print(j)
    google_back_menu = input("1) Exit\n2) Restart\n:: ")
    if google_back_menu == "2":
        google()
    else:
        menu()


# menus for end of functions
def back_menu0():
    wiki_search1 = ""
    wiki_menu = input("0) Restart\n1) Go to menu\n:: ")\

    if wiki_menu == "0":
        wiki()

    if wiki_menu == "1":
        menu()

# end of back menu


# start of back menu for calculator
def back_menu1():
    calculator_menu = input("1) Exit\n2) Restart\n:: ")

    if calculator_menu == "1":
        menu()

    if calculator_menu == "2":
        calculator()

    else:
        menu()
# end of back menu for calculator


# start of back menu for bash
def back_menu2():

    back_menu2 = input("0) Restart\n1) Exit\n:: ")

    if back_menu2 == "0":
        bash()

    else:
        menu()
# end of back menu for bash

menu()
