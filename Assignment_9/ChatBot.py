import streamlit as st
import user_database
import message_database 
from models import  User
from sqlmodel import  Session ,select
from Database import connect_to_database



engine = connect_to_database()



col1 =st.columns(1)
options = ["Sign-Up", "Sign In"]
selected_option = st.sidebar.selectbox("Choose an option:", options)
def insert_new_user():
            
            if selected_option == "Sign-Up":
                st.markdown("<h2 style='text-align: left; color:red'>SIGN-UP</h2>", unsafe_allow_html=True)
                with st.form(key='signup_form',clear_on_submit=True, border=True):
                        
                        name = st.text_input("Name")
                        email = st.text_input("Email")
                        username = st.text_input("Username")
                        password = st.text_input("Password", type="password")
                        submit_button = st.form_submit_button(label='Sign Up')

                        # Handle form submission
                        if submit_button:
                            if name and email and username and password:
                                with Session(engine) as session:
                                    result = select(User).where(User.email == email)
                                    user = session.exec(result).first()  
                                    if user:
                                        st.warning("this email already registered")
                                    
                                    else:
                                        user_database.user_process(name, email, username, password)
                                        st.success("User created successfully!")
                            else:
                                 st.error("Please fill in all fields.")


def send_message(username, user_id):
   
    if "messages" not in st.session_state:
          st.session_state.messages = []
    st.session_state["items_1"] = username
    item_1 =st.session_state["items_1"]
    
    st.session_state["items_2"] = user_id
    item_2 =st.session_state["items_2"]
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
     with st.chat_message(message['type']):
        st.write(message['text'])
    if user_text_message := st.chat_input("Say something", disabled=False):
        ai_text_message = message_database.message_process(user_text_message,username=item_1 , user_id=item_2)
        with st.chat_message("user"):
             st.write(user_text_message)

        with st.chat_message("ai"):
                st.write(ai_text_message)
   

def sign_in():
        if selected_option == "Sign In":
            st.markdown("<h2 style='text-align: left; color:green'>SIGN-IN</h2>", unsafe_allow_html=True)
                #with st.form(key='signin_form', clear_on_submit=True, border=True):
                    
            username = st.text_input("Username")
            
                        # print("hi user",username)
            if username:
                password = st.text_input("Password", type="password")
                               
                if password:
                    my_btn_3 = st.button(label='Sign In')
                                # print('hi pass:',password)
                    if my_btn_3:
                        with Session(engine) as session:
                            statement = select(User).where(User.username == username, User.password == password)
                            user = session.exec(statement).first()
                            if user:
                                username = user.username
                                
                                user_id = user.id
                                
                                
                                if username and user_id is not None:
                                    result = send_message(username,user_id)
                                                    
                                    return result   
                                           
        return None                                    
                                



if __name__ == "__main__":
     insert_new_user()
     sign_in()
                            
                      

