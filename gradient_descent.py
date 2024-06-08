# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online
import numpy as np
x = np.array([6.1101, 5.5277, 8.5186, 7.0032, 5.8598])
y = np.array([17.592, 9.1302, 13.662,  11.854,6.8233])
w = 0
b = 0



def compute_gradient(x,y,w,b):
    m = x.shape[0];
    dj_dw = 0;
    dj_db = 0;
    prediction_model = 0;
    total_dj_dw = 0;
    total_dj_db = 0;
    for index, element in enumerate(x):
        prediction_model = (w * element) + b;
        dj_db = prediction_model - y[index];
        dj_dw = (prediction_model - y[index])*element

        total_dj_dw = dj_dw + total_dj_dw
        total_dj_db = dj_db + total_dj_db
    
    dj_dw = total_dj_dw/m;
    dj_db = total_dj_db/m;

    return dj_dw, dj_db

def total_sum(x,y,w,b):
    prediction_model = 0;
    cost = 0;
    total_cost = 0;
    m = x.shape[0] 
    for index, element in enumerate(x):

        prediction_model = (w * element) + b;
        cost = (prediction_model - y[index]) **2
        total_cost = cost + total_cost
        print(f" predicton model is {prediction_model}")
        print(f" cost is {cost}")

    total_cost = total_cost/(2 * m)
    print(f"total cost is {total_cost}")
    return total_cost



dj , dw = compute_gradient(x,y,w,b)
print(f"the value is {dj}, and {dw}")
