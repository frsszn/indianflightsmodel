import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    st.title("Indian Flight Data Prices Exploration")
    st.image("https://i.ytimg.com/vi/IoItzY9C_a4/sddefault.jpg", caption='Source: google.com')
    st.markdown("## Latar Belakang")

    st.markdown('''Maskapai menetapkan harga untuk layanan mereka dengan tujuan memaksimalkan keuntungan. Penentuan harga tiket pesawat semakin rumit dari waktu ke waktu dan kini sebagian besar ditentukan oleh sistem manajemen pendapatan berbasis komputer.

        Project ini akan dibuat menggunakan algoritma KNN, SVM, Decision Tree, Random Forest, dan Boosting''')

    st.markdown("## Dataset")
    st.markdown('''Dataset Indian Flight Data yang diambil dari kaggle.com''')
    df = pd.read_csv('dataset.csv')
    st.write(df)   

    st.markdown("## Exploratory Data Analysis")
    st.markdown("### Flight Prices Distribution")
    # Histogram distribusi harga tiket
    fig = plt.figure(figsize=(12, 6))
    sns.histplot(df['price'], bins=40, kde=True, color='skyblue')
    plt.title("Distribusi Harga Tiket Penerbangan", fontsize=14, weight='bold')
    plt.xlabel("Harga Tiket (Rupee)")
    plt.ylabel("Jumlah Penerbangan")
    plt.grid(alpha=0.3)
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Average Flight Prices per Airline")
    # Urutkan maskapai berdasarkan harga rata-rata biar plot-nya rapi
    avg_price = df.groupby('airline')['price'].mean().sort_values(ascending=False).reset_index()

    fig = plt.figure(figsize=(12,5))
    sns.barplot(
        x='airline', 
        y='price', 
        data=avg_price, 
        palette='viridis'
    )
    plt.title("Rata-Rata Harga Tiket per Maskapai", fontsize=14, weight='bold')
    plt.xlabel("Maskapai")
    plt.ylabel("Harga Rata-Rata (Rupee)")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Departure Time vs Flight Prices")
    # Urutkan kategori waktu biar visual rapih
    order = ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Late_Night']

    fig = plt.figure(figsize=(12,6))
    sns.boxplot(
        x='departure_time',
        y='price',
        data=df,
        order=order,
        palette='crest'
    )
    plt.title("Perbandingan Harga Tiket Berdasarkan Waktu Keberangkatan", fontsize=14, weight='bold')
    plt.xlabel("Waktu Keberangkatan")
    plt.ylabel("Harga Tiket (Rupee)")
    plt.grid(alpha=0.3)
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Flight Duration vs Flight Prices")
    fig = plt.figure(figsize=(10,6))
    sns.regplot(
        x='duration',
        y='price',
        data=df,
        scatter_kws={'alpha':0.3, 'color':'steelblue'},
        line_kws={'color':'red', 'lw':2}
    )
    plt.title('Hubungan antara Durasi Penerbangan dan Harga Tiket', fontsize=13, fontweight='bold')
    plt.xlabel('Durasi Penerbangan (jam)')
    plt.ylabel('Harga Tiket (Rupee)')
    plt.grid(True)
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Number of Stops vs Flight Prices")
    fig = plt.figure(figsize=(10,6))
    sns.boxplot(x='stops', y='price', data=df, palette='viridis')

    plt.title('Perbandingan Harga Tiket Berdasarkan Jumlah Transit', fontsize=13, fontweight='bold')
    plt.xlabel('Jumlah Transit')
    plt.ylabel('Harga Tiket')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Most Frequent Destination City")
    fig = plt.figure(figsize=(10,6))
    sns.countplot(
        x='destination_city', 
        data=df, 
        order=df['destination_city'].value_counts().index, 
        palette='magma'
    )

    plt.title('Frekuensi Kota Tujuan Penerbangan', fontsize=13, fontweight='bold')
    plt.xlabel('Kota Tujuan')
    plt.ylabel('Jumlah Penerbangan')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    st.pyplot(fig)

    st.markdown('___')
    st.markdown("### Comparison of The Number of Flights per Airline")
    # Hitung jumlah penerbangan per maskapai
    airline_counts = df['airline'].value_counts()

    # Buat pie chart
    fig = plt.figure(figsize=(8,8))
    plt.pie(
        airline_counts,
        labels=airline_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=sns.color_palette('pastel'),
        wedgeprops={'edgecolor': 'black'}
    )
    plt.title('Persentase Jumlah Penerbangan Tiap Maskapai', fontsize=14, fontweight='bold')
    st.pyplot(fig)

if __name__ == '__main__':
    run()



