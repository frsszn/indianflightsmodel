import streamlit as st
import pandas as pd
import pickle


def run():
    # Load model
    with open('best_model_rf.pkl', 'rb') as file_1:
        best_model_rf = pickle.load(file_1)

    st.title("✈️ Prediksi Harga Tiket Pesawat")

    # Form input
    with st.form(key='flight'):
        airline = st.selectbox("Pilih Airline", 
                            ('SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'))
        deptime = st.selectbox("Pilih Waktu Berangkat", 
                            ('Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'))
        stops = st.selectbox("Masukan Jumlah Transit", 
                            ('zero', 'one', 'two_or_more'))
        arrtime = st.selectbox("Masukan Waktu Sampai", 
                            ('Night', 'Morning', 'Early_Morning', 'Afternoon', 'Evening', 'Late_Night'))
        destct = st.selectbox("Masukan Kota Tujuan", 
                            ('Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai', 'Delhi'))
        kelas = st.selectbox("Masukan Class", 
                            ('Economy', 'Business'))
        duration = st.slider("Masukan Durasi Penerbangan (jam)", min_value=0, max_value=50, value=5)
        day = st.number_input("Masukan Hari Tersisa sebelum Penerbangan", min_value=0, max_value=60, value=7)

        submit = st.form_submit_button('Predict')

    # Saat tombol ditekan
    if submit:
        data = pd.DataFrame([{
            'airline': airline,
            'departure_time': deptime,
            'stops': stops,
            'arrival_time': arrtime,
            'destination_city': destct,
            'class': kelas,
            'duration': duration,
            'days_left': day
        }])

        prediksi = best_model_rf.predict(data)
        st.success(f" **Harga tiket diprediksi sekitar: ₹{prediksi[0]:,.0f}**")

if __name__ == '__main__':
    run()
