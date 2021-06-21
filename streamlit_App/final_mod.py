# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:56:31 2021

@author: romas
"""

import streamlit as st
import pickle

from sklearn.linear_model import LogisticRegressionCV



pickle_in = open("final_mod.pkl","rb")
classifier=pickle.load(pickle_in)
def mood_recog(Price,Hours,Art):
    prediction=classifier.predict([[Price,Hours,Art]])
    print(prediction)
    return prediction
def main():
    st.title("Art Classification Model")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:blue;text-align:center;">Student Mood Recognition </h2>
    </div>
    """
    name = st.text_input("Name: ")
    email = st.text_input("Email Id: ")
    price = st.text_input("Price: ")
    day = st.text_input("Enter Day: ")
    month=st.text_input("Enter Month: ")
    year=st.text_input("Enter Year: ")
    country=st.text_input("Country: ")
    state=st.text_input("State: ")
    hours=st.text_input("Number of Hours Devoted: ")
    art=st.text_input("Type of Art: ")
    if st.button("Know More"):
        html_temp = """
                        
                        <div>
                        <h3 style="color:red;text-align:left;">0 =  Digital Art </h3>
                        <h3 style="color:red;text-align:left;">1 = Physical Art </h3>
                       </div>
                    """
        st.markdown(html_temp,unsafe_allow_html=True)
    if st.button("Predict"):
        result = mood_recog(price,hours,art)
        if int(result)==0:
            st.success("Your Art Piece cannot be accepted for sale on the blockchain.")
        if int(result)==1:
            st.success("Your Art Piece is accepted for sale on the blockchain.")
        import ics as icsneo
        from ics import Calendar, Event
        final = str(year) + "-" +str(month) + "-" +str(day) + " 00:00:00"
        print(final)
        c = Calendar()
        e = Event()
        e.name = "Your Art piece was "
        e.begin = final
        c.events.add(e)
        c.events
        with open('my.ics', 'w') as my_file:
            my_file.writelines(c)
        import smtplib
        from email.message import EmailMessage
    
        EMAIL_ADDRESS ="weecaree4youu@gmail.com"
        EMAIL_PASSWORD ="glvqfnhrbcjdjsqc"
    
        msg = EmailMessage()
        msg['Subject'] = 'Update regarding your ART status in the blockchain: '
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email
    
        msg.set_content('Your Art Piece is accepted for sale on the blockchain."')
    
        files = ['my.ics']
    
        for file in files:
            with open(file,'rb') as f:
                file_data = f.read()
                file_name = f.name
    
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream',filename=file_name)
    
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        



if __name__=='__main__':
    main()