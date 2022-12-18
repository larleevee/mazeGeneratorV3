import PySimpleGUI as sg

#THEME MUST GO HERE, IF NOT IT HAS A HISSY FIT :(
sg.theme("DarkPurple1")

#Stored as a 2D array
MainMenu_Layout = [
    [sg.Text(" ")], 
    [sg.Button("Login", size=(50,1))],
    [sg.Button("Create Account", size=(50,1))],
    [sg.Button("View Leader Board", size=(50,1))],
    [sg.Button("Exit", size=(50,1))],
    [sg.Text(" ")] #blank line (spacing purposes)
]

Login_Layout = [
    [sg.Text(" ")],
    [sg.Text("Username", size=(10,1)), sg.InputText(key="username")],
    [sg.Text("Password", size=(10,1)), sg.InputText(key="password")],
    [sg.Text(" ")],
    [sg.Button("Login", size=(51,1))],
    [sg.Button("Main Menu", size = (25,1)), sg.Button("Exit", size = (24,1))]
]

CreateAccount_Layout = [
    [sg.Text(" ")],
    [sg.Text("Username", size=(10,1)), sg.InputText(key="username")],
    [sg.Text("Password", size=(10,1)), sg.InputText(key="password")],
    [sg.Text("Password", size=(10,1)), sg.InputText(key="confPassword")],
    [sg.Text(" ")],
    [sg.Button("Create Account", size=(51,1))],
    [sg.Button("Main Menu", size = (25,1)), sg.Button("Exit", size = (24,1))]
]

LeaderBoard_Layout = [


]

Pick_Layout = [
    [sg.Text(" ")],
    [sg.Button("Easy", size=(10, 1)), sg.Button("Medium", size=(10, 1)), sg.Button("Hard", size=(10, 1))],
    [sg.Text(" ")]
]

