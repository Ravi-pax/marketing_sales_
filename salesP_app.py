# import packages
import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from sklearn.preprocessing import StandardScaler

# Load the model
model_path = r'pipeline_model.pkl'

with open(model_path, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define your 'predictor' function here
def predictor(array):
    try:
        output = loaded_model.predict(array)
        return output
    except Exception as e:
        st.error(f'Error during prediction: {str(e)}')
        return None

def main():
    # desinining 

    st.title('Sales Prediction Via Ads Expenditure')
    st.subheader('This is how input data should look like')

    st.image('.\media_files\data_should_like.PNG')

    # Option to upload a JSON file or input three s
    option = st.radio("Choose input method:", ("Upload JSON file", "Input three values"))

    scaled_data = None  # Initialize scaled_data outside the if blocks

    if option == "Upload JSON file":
        upload_ = st.file_uploader('Upload your JSON file', type='json')

        if upload_ is not None:
            try:
                json = pd.read_json(upload_)

                st.dataframe(json)

                df = pd.DataFrame(json)

                # Transpose the DataFrame
                df_transposed = df.transpose()


                # Scale down
                scaler = StandardScaler()
                scaled_data = scaler.fit_transform(df_transposed)
                scaled_data = scaled_data.T
                
                # back to dataframe (scaled)
                scaled_data = pd.DataFrame(scaled_data)

                if scaled_data is not None:  # Check if scaled_data is not None before passing it to predictor
                    prediction = predictor(scaled_data)

                if prediction is not None:
                    result_df = pd.DataFrame(prediction, columns=['Prediction'])
                    st.subheader('Model Prediction is here')
                    st.dataframe(result_df)

                    # Convert to text
                    tex = result_df.to_latex(index=False)
                    # Downloadable option
                    st.download_button("Download as a text file", tex, file_name="prediction.txt")

            except Exception as e:
                st.error(f'Error processing data: {str(e)}')

    else:
        feature1 = st.number_input("TV:", value=0.0)
        feature2 = st.number_input("Radio:", value=0.0)
        feature3 = st.number_input("Social Network:", value=0.0)

        collects = pd.DataFrame({"feature1": [feature1], "feature2": [feature2], "feature3": [feature3]})

        if st.button("Predict"):
            try:
                st.dataframe(collects)
                collects_Transpobe = collects.transpose()
                # Scale down
                scaler = StandardScaler()
                scaled_data = scaler.fit_transform(collects_Transpobe)

                scaled_data = scaled_data.T

                # back to dataframe (scaled)
                scaled_data = pd.DataFrame(scaled_data)

                if scaled_data is not None:  # Check if scaled_data is not None before passing it to predictor
                    prediction = predictor(scaled_data)

                if prediction is not None:
                    result_df = pd.DataFrame(prediction, columns=['Prediction'])
                    st.subheader('Model Prediction is here')
                    st.dataframe(result_df)

                    # Convert to text
                    tex = result_df.to_latex(index=False)
                    # Downloadable option
                    st.download_button("Download as a text file", tex, file_name="prediction.txt")

            except Exception as e:
                st.error(f'Error processing data: {str(e)}')

if __name__ == "__main__":
    main()
