import streamlit as st

#with st.container(height=400, border=True):
#    pass

st.markdown('''
<style>
 
  .cmain {
        background-color:#1e293b;
        margin-bottom:0px;
        padding-botom:0px;
        width:700px;
        transform-origin:top;
        transform:scaleY(1.32);
    
        
        border-radius: 7px;
        /*border: 1px solid #ffffff;*/
        height: 303px;
             }
    body {
            overflow: hidden
            } 
</style>

'''
, unsafe_allow_html=True)

x=st.markdown('<div class="cmain"</div>',unsafe_allow_html=True)

