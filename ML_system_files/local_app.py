# import packages
import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from sklearn.preprocessing import StandardScaler

## model 1 
#model_path = r'model3.pkl'

#with open(model_path,'rb') as model_file:
#    loaded_model = pickle.load(model_file)

#model 2 (pipeline)
model_path = r'pipeline_model.pkl'

with open(model_path,'rb') as model_file:
    loaded_model = pickle.load(model_file)


#model 3 (LR)
#model_path = r'model4.pkl'

#with open(model_path,'rb') as model_file:
#    loaded_model4 = pickle.load(model_file)


## model prediction process
## model takes as 2d numpy arrau
def predicitor(array):
    try:
        oupt = loaded_model.predict(array)
        return oupt
    except Exception as ee:
        st.error(f'Error during prediction {str(ee)}') # use to represent error
        return None

# main body
def main():
    st.title('Sales Prediciton App')

    # upload csv file
    upload_ = st.file_uploader('Upload your csv file',type=['csv'])

    if upload_ is not None:
        try:
            df = pd.read_csv(upload_)

            # notify
            st.subheader('Data is Uploaded')
            st.dataframe(df)
            
            # scale down
            from sklearn.preprocessing import StandardScaler
            sclr = StandardScaler()
            sclr.fit(df)
            input_data = sclr.transform(df)
            
            # convert into 2d
            #input_data = df.values

            prediction = predicitor(input_data)
            
            if prediction is not None:
                result_df = pd.DataFrame(prediction,columns=['Prediction'])
                st.subheader('Model Prediction is here')
                st.dataframe(result_df)
                
                #conver to text
                tex = result_df.to_latex(index=False)
                # downloadable option
                st.download_button("downlon as a text file",tex)

        except Exception as e:
            st.error(f'Error processing data: {str(e)}')

if __name__ == "__main__":
    main()

