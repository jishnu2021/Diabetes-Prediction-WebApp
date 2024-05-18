import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open('C:/Users/PC/Desktop/Diabetis/trained_model.sav', 'rb'))

def diabetisprediction(input_data):
    # Changing the input data to a numpy array
    input_nparray = np.asarray(input_data, dtype=float)  # Ensure conversion to float

    # Reshape the array as we are predicting for one instance
    input_data_reshape = input_nparray.reshape(1, -1)

    # Make a prediction
    prediction = loaded_model.predict(input_data_reshape)
    
    if prediction[0] == 0:
        return "The person is not diabetic"
    else:
        return "The person is diabetic"

def main():
    # Giving the title
    st.title('Diabetes Prediction Web App')
    
    # Getting the input data from the user
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('BloodPressure level')
    SkinThickness = st.text_input('SkinThickness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI level')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of the person')
    
    diagnosis = ''
    
    # When the button is pressed, make the prediction
    if st.button('Diabetes Test Result'):
        try:
            # Convert inputs to float
            input_data = [
                float(Pregnancies),
                float(Glucose),
                float(BloodPressure),
                float(SkinThickness),
                float(Insulin),
                float(BMI),
                float(DiabetesPedigreeFunction),
                float(Age)
            ]
            diagnosis = diabetisprediction(input_data)
        except ValueError:
            diagnosis = "Please enter valid numeric values for all inputs."
        
    st.success(diagnosis)

if __name__ == '__main__':
    main()
