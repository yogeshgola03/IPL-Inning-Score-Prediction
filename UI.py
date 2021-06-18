import streamlit as st

import keras
import numpy as np

def team_code(team):
    if team == 'Kolkata Knight Riders':
        return 0
    elif team == 'Chennai Super Kings':
        return 1
    elif team == 'Rajasthan Royals':
        return 2
    elif team == 'Mumbai Indians':
        return 3
    elif team == 'Kings XI Punjab':
        return 4
    elif team == 'Royal Challengers Bangalore':
        return 5
    elif team == 'Delhi Daredevils':
        return 6
    elif team == 'Sunrisers Hyderabad':
        return 7
    
model = keras.models.load_model('Score_Prediction_50')

def prediction(bat_team, bal_team, overs, runs, wickets, runs_5, wickets_5):
    test = np.array([team_code(bat_team), team_code(bal_team), runs, wickets, overs, runs_5, wickets_5])
    test = test.astype('float32')
    test = test[np.newaxis,:]
    pred = model.predict(test)
    return int(pred[0][0])

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;padding:13px"> 
    <h1 style ="color:white;text-align:center;">IPL Inning Score Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    st.info("This model predict the final score of a inning on the basis of current scorecard. This model is build using Artificial Neural Networks.")
    # following lines create boxes in which user can enter data required to make prediction 
    bat_team = st.selectbox('Batting Team',("Chennai Super Kings","Kolkata Knight Riders","Rajasthan Royals","Mumbai Indians","Kings XI Punjab","Royal Challengers Bangalore","Delhi Daredevils","Sunrisers Hyderabad"))
    bal_team = st.selectbox('Bowling Team',("Mumbai Indians","Kolkata Knight Riders","Chennai Super Kings","Rajasthan Royals","Kings XI Punjab","Royal Challengers Bangalore","Delhi Daredevils","Sunrisers Hyderabad")) 
    overs = st.number_input("Overs (>=5.0) e.g. 8.1", min_value=5.0, max_value=20.0, value=20.0, step=0.1)
    runs = st.number_input("Runs (e.g. 68)",min_value=0, value=0, step=1)
    wickets = st.number_input("Wickets (e.g. 4)",min_value=0, max_value=10, value=0, step=1)
    runs_5 = st.number_input("Runs Scored in last 5 overs (e.g. 42)",min_value=0, value=0, step=1)
    wickets_5 = st.number_input("Wickets taken in last 5 overs (e.g. 2)",min_value=0, value=0, step=1)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict Score"): 
        result = prediction(bat_team, bal_team, overs, runs, wickets, runs_5, wickets_5) 
        st.success('The Final Predicted Score is :  {}'.format(result))
     
if __name__=='__main__': 
    main()




