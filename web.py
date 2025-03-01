import streamlit as st
import function

def add_todo():
    todo = st.session_state["New_Todo"]
    if todo.strip() != "":
        todos = function.get_todos()
        todos.append(todo+"\n")
        function.send_todos(todos)

def complete():
    todos = function.get_todos()
    for todo in todos:
        if st.session_state[f"{todo}_Todo_Complete"]:
            todos = function.get_todos()
            todo_completed = todo
            todos.remove(todo_completed)
            function.send_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

todos = function.get_todos()

for todo in todos:
    st.checkbox(todo,on_change=complete, key=f"{todo}_Todo_Complete")

st.text_input(label="Enter a Todo", 
              placeholder="Add new todo....", 
              on_change=add_todo, 
              key='New_Todo')