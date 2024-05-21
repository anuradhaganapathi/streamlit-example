import numpy as np
import pandas as pd
import streamlit as st
import boto3
import json
import nltk


email = st.text_area("Text to be analyzed",key='email')

btn1 = st.button('Analyse')

if btn1:
    st.write(email)

 
endpoint = 'blazingtext-2024-05-18-20-34-01-612'
 
runtime = boto3.client('sagemaker-runtime',region_name="eu-north-1")
#messages = [
 #               # Spam
  #              'Click on below link, provide your details and win this award' ,
   #             'Best summer deal here',
    #            #ham
     #           'See you in the office on Friday.'
#
#]

messages = [email]

tokenized_message = [' '.join(nltk.word_tokenize(mesaage)) for mesaage in messages]
payload = {"instances" : tokenized_message}
payload = json.dumps(payload)

# Convert the input data to JSON format
#payload = json.dumps(input_data)
# Send image via InvokeEndpoint API
response = runtime.invoke_endpoint(EndpointName=endpoint, ContentType='application/json', Body=payload.encode())

# Unpack response
result = json.loads(response['Body'].read().decode())
print(result)

for res in result:
    final_value = res['label']

for test in final_value:
    print(test.replace('__label__',''))