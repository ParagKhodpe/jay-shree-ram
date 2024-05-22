import pandas as pd
import streamlit as st
from sklearn.neighbors import KNeighborsRegressor

st.title('model Deployment:KNeighboursregression')

st.sidebar.header('user input parameters')

def user_input_features():
    engine_size=st.sidebar.number_input('Insert the Size')
    cylinders=st.sidebar.number_input('Insert the cylinders')
    fuel_consumption_city=st.sidebar.number_input('Insert the fuel in city')
    make=st.sidebar.selectbox('make',('1','0','2','3','4','5'))
    model=st.sidebar.selectbox('model',('0','1','100','150','200','500','1000','1200','1400','1500'))
    vehicle_class=st.sidebar.selectbox('class',('0','1','2','11','12','15'))
    transmission=st.sidebar.selectbox('transmission',('0','1','2','4','5','6','9'))
    fuel_type=st.selectbox('fuel type',('0','1','2','3','4','5',))
    data  = {'engine_size':engine_size,
             'cylinders':cylinders,
             'fuel_consumption_city':fuel_consumption_city,
             'make':make,
             'model':model,
             'vehicle_class':vehicle_class,
             'transmission':transmission,
             'fuel_type':fuel_type}
    features=pd.DataFrame(data,index=[0])
    return features

df=user_input_features()
st.subheader('user_input_parameters')
st.write(df)

co2=pd.read_csv("/content/co2_emissions (1).csv")
co2=drop([["fuel_consumption_comb(l/100km)","fuel_consumption_hwy","fuel_consumption_comb(mpg)"]],inplace=True)
x=co2.iloc[:,:-1]
y=co2.iloc[:,-1]
clf=KNeighboursregression()
clf.fit(x,y)

prediction =clf.predict(df)
prediction_proba=clf.predict_proba(df)

st.subheader('prediction result')
st.write('yes' if prediction_proba[0][1]>0.5 else 'no')
st.subheader('prediction probability')
st.write(prediction_proba)

