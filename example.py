import streamlit as st


x = st.slider('x')
# st.write(x, 'squared is', x*x)

url = st.text_input('Enter URL')
# st.write('The Entered URL is', url)

import pandas as pd
import numpy as np

df = pd.read_csv('./data/football_data.csv')
if st.checkbox('Show dataframe'):
    st.write(df)

# SelectBox
option = st.selectbox('Which Club do you like best?', df['Club'].unique())
'You selected: ', option

# MultiSelect
options = st.multiselect('What are your favorite clubs?', df['Club'].unique())
'You selected', options
