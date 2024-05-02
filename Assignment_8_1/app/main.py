import streamlit as st
st.title("Counter")

col1, col2, col3 = st.columns(3)


class main:
    def __init__(self):
        # Initialize a session state variable
        if "items" not in st.session_state:
            st.session_state["items"] = 0
        self.items = st.session_state["items"]
        
        with col3:
            self.plus_btn = st.button("➕", key='plus', type='primary')
            if self.plus_btn:
                  self.plus()
        with col1:
            self.minus_btn = st.button("➖", key='minus', type='primary')
            if self.minus_btn:
               self.minus()

    def minus(self):
            with col2:
                st.session_state["items"] = st.session_state["items"] - 1
                return st.header(self.items)
            
    def plus(self):
        with col2:
                st.session_state["items"] = st.session_state["items"] + 1
                return st.header(self.items)
        


if __name__ == "__main__":
    main()
    