import PySimpleGUI as sg
from GUI_LAYOUT import *
from GameLoop import mainCode

def MainMenu():
    """
    buttons = Login, Create Account, View Leader board, Exit
    inputs = none
    """

    window = sg.Window("Main Menu", MainMenu_Layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Login":
            Login()
        if event == "Create Account":
            CreateAccount()
        if event == "View Leader Board":
            print("View Leader Board")

    window.close()


def Login():
    """
    buttons = Login, Main Menu, Exit
    inputs = Username, Password
    """

    window = sg.Window("Login", Login_Layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        if event == "Login":
            #check if input == valid
            Pick()
        if event == "Main Menu":
            window.close()

    window.close()

def CreateAccount():
    """
    buttons = Create Account, Main Menu, Exit
    inputs = Username, Password, Confirm Password
    """

    window = sg.Window("Create Account", CreateAccount_Layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Create Account":
            if values["password"] != values["confPassword"]:
                sg.popup("ERROR", "Passwords do not match!")
            else:
                Pick()

        if event == "Main Menu":
            window.close()

def Pick():
    """
    buttons = Start, Main Menu, Exit
    inputs = Size
    """

    window = sg.Window("Pick", Pick_Layout)
    
    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break

        if event == "Easy":
            difficulty = 60
            mainCode(difficulty)
        if event == "Medium":
            difficulty = 30
            mainCode(difficulty)
        if event == "Hard":
            difficulty = 15
            mainCode(difficulty)

    return difficulty

MainMenu()

