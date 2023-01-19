import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"  # (session_state) object type of st. contains pairs of data user enters.
    #  we call the key of that pair and get the value of that pair. session state dict for the widgets
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""  # to clear the input box after user hits enter


st.title("My todo app")
st.subheader("This is my todo app.")
st.write("This is to increase productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  # each checkbox will have unique key. store ea checkbox in variable
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()  # needed for checkboxes

st.text_input(label=" ", placeholder="Add a new todo...", on_change=add_todo, key="new_todo")
