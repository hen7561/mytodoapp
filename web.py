import streamlit as st
import func


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + "\n")
    func.write_todos(todos)


todos = func.get_todos()
st.title("My todo app")
st.subheader("This is my todo app")
st.write("this app is to increase you productivity")

for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Enter a new todo..", on_change=add_todo, key='new_todo')
