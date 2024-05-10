import numpy as np
import pandas as pd
import streamlit as st
import boto3
import json

email = st.text_area("Text to be analyzed",key='email')

btn1 = st.button('Analyse')

if btn1:
    st.write(email)

 
endpoint = 'blazingtext-2024-05-10-13-30-15-678'
 
runtime = boto3.client('sagemaker-runtime',region_name="eu-north-1")
messages = [
                # Spam
                'Click on below link, provide your details and win this award' ,
                'Best summer deal here',
                #ham
                'See you in the office on Friday.'

]

# Set the input data
input_data = {
        'data': ['input_value_1', 'input_value_2']
    }

    # Convert the input data to JSON format
payload = json.dumps(input_data)
# Send image via InvokeEndpoint API
response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/json', Body=payload)

# Unpack response
result = json.loads(response['Body'].read().decode())