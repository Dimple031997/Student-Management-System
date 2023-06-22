
import streamlit as st
import firebase_admin
from firebase_admin import db
@st.cache
def runonce():
    cred=firebase_admin.credentials.Certificate("key.json")
    app=firebase_admin.initialize_app(cred,{'databaseURL':'https://august-5d0d1-default-rtdb.firebaseio.com/'})
runonce()
mymenu=st.sidebar.selectbox("MENU",("Home","Exam","Result","Information"))
st.title("Student Management System")
st.header("WELCOME STUDENT")
st.image("https://acegif.com/wp-content/uploads/2021/4fh5wi/welcome-15.gif")
if(mymenu=="Exam"):

    st.text("Here you can give Maths Exam ,after exam you can check your result")
    st.markdown('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSd6CbVrmusVvdXhi5pZpy02YMBGYWN4xcutuKxBv3mNsnP_Fw/viewform?embedded=true" width="640" height="1330" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>',unsafe_allow_html=True)
    
elif(mymenu=="Result"):
    with st.form("Result"):
        rollno=st.text_input("Enter your Roll Number")
        submitted=st.form_submit_button("View Result")
        if submitted:
            data=db.reference("/"+rollno).get()
            st.table({"Acquired Marks":{"Maths":data['Maths'],"Hindi":data['Hindi'],"English":data['English']},"Total Marks":{"Maths":100,"Hindi":100,"English":100},"Grade":{"Maths":data['Maths grade'],"Hindi":data['Hindi grade'],"English":data['English grade']}})
            st.subheader("Result:"+data['Result'])
            st.image("https://www.eventstodayz.com/wp-content/uploads/2020/01/Congratulations-GIF8-1.gif-1.gif",width=600)
elif(mymenu=="Information"):
    with st.form("Result"):
        rollno=st.text_input("Enter your Roll Number")
        submitted=st.form_submit_button("View Profile")
        if submitted:
            data=db.reference("/"+rollno).get()
            st.write("Name:",data['Name'])
            st.write("Age:",data['Age'])
            st.write("City:",data['City'])
            st.write("Email:",data['Email'])
            st.image("https://www.futuraconverting.com/fileadmin/user_upload/news/foto-news-THANKS-MAIC-animata.gif")