import function
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")
edit_button=sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box=sg.Listbox(values=function.get_todos(),key="todos",enable_events=True,size=[45,10])

window = sg.Window('My to-do app',layout=[[label],[input_box,add_button,complete_button],[list_box,edit_button,exit_button]],font=('Helvetica',20))
while True:
 event,values=window.read()
 print(1,event)
 print(2,values)
 print (3,values['todos'])
 match event:
     case "Add":
         todos=function.get_todos()
         new_todo=values['todo']+"\n"
         todos.append(new_todo)
         function.write_todos(todos)
         window['todos'].update(values=todos)
     case "Edit":
          todo_to_edit = values['todos'][0]
          new_todo=values['todo']
          todos=function.get_todos()
          index=todos.index(todo_to_edit)
          todos[index]=new_todo
          function.write_todos(todos)
          window['todos'].update(values=todos)

     case "Complete":
         todo_to_complete = values['todos'][0]
         todos=function.get_todos()
         todos.remove(todo_to_complete)
         function.write_todos(todos)
         window['todos'].update(values=todos)
         window['todo'].update(value = '')
     case "Exit":
         break
     case "todos":
         window['todo'].update(value=values['todos'][0])
     case sg.WIN_CLOSED:
         break
window.close()