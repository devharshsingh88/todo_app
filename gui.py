import functions
import PySimpleGUI27 as sg

label = sg.Text("Type in a to-do")
input_box = sg.Input(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
print("Hello")
window.read()
window.close()