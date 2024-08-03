import streamlit as st
import functions

# read the file and holds the list
todos = functions.read_file()

# callback func to get a newly added item using text box
def add_todo():
    todo = st.session_state["new_todo"]  + "\n"
    print(todo)
    todos.append(todo)
    functions.write_file(todos)
    # st.session_state["new_todo"] = ''

st.title("My Todos App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# to render all the todos item on the page
for todo in todos:
    st.checkbox(todo)

user_todo = st.text_input(label='', placeholder="Add a todo item", on_change=add_todo, key="new_todo")