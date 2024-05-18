import numpy as np
import pickle

loaded_model = pickle.load(open('C:/Users/PC/Desktop/Diabetis/trained_model.sav','rb'))

input=(2,197,70,45,543,30.5,0.158,53)

#changing the input data to numpy array
input_nparray = np.asarray(input)

input_data_reshape = input_nparray.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshape)
print(prediction)

if (prediction[0]==0):
  print("the person is not diabetic")
else:
  print("the person is diabetic")