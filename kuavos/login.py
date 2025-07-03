import streamlit as st
#l,s=st.tabs(["Login","Sign up"])





with st.container(height=300, border=True):
        
        for i in range(1):
            st.write("\n")
        email=st.text_input("Email")
        st.write("\t")
        pasw=st.text_input("Password", type="password")


        
        st.write("\t",end="")

        n,col1,l,col2,e=st.columns(5, gap="medium")
        
        with col1:
            
            login=st.button("Login")
        with col2:
            signup=st.button("Sign Up")
      

