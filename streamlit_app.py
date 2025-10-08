import streamlit as st
import eda, model

with st.sidebar:
        st.title('Page Navigation')
        # input
        page = st.radio('Page', ['EDA', 'Model Demo'])

        st.write('# About')
        st.write('''
                 Page ini adalah informasi data dan demo dari model prediksi harga tiket pesawat di India''')
        
if page == 'EDA':
        eda.run()

else:
        model.run()
        