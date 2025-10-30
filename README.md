# Indian Flights Prediction Model

## Repository Outline
1. description.md - Penjelasan gambaran umum project
2. P1M2_Farissthira.ipynb - Notebook yang berisi Objective Business, Exploratory Data Analysis, Pembuatan Model, dan kesimpulan project.
3. P1M2_Farissthira_inf.ipynb - Notebook ini berisi contoh inference dari model yang sudah kita buat.
4. streamlit_app.py - Python script ini adalah script utama dalam deployment yang berisi navigation.
5. eda.py - Python Script ini berisi script Exploratory Data Analysis untuk deployment.
6. model.py - Python Script ini berisi script form deployment untuk penggunaan model.
7. best_model_rf.pkl - Model yang digunakan.
8. dataset.csv - Dataset Flight Prices India.
9. url.txt - File yang berisi informasi URL project ini.
10. P1M2_Farissthira_Conceptual - File berisi jawaban conceptual problem.

## Problem Background
Harga tiket pesawat dipengaruhi oleh berbagai faktor, seperti durasi penerbangan, jumlah hari sebelum keberangkatan, waktu tiba, dan waktu berangkat, serta faktor lainnya. Maskapai dapat menurunkan harga tiket ketika ingin meningkatkan permintaan pasar, dan sebaliknya menaikkan harga ketika ketersediaan tiket semakin sedikit. Harga juga dapat bergantung pada berbagai faktor lain, di mana masing-masing faktor memiliki aturan dan algoritma tertentu dalam penetapan harga. Machine Learning (ML) memungkinkan kita untuk mengidentifikasi aturan-aturan tersebut dan memodelkan variasi harga secara lebih akurat.

## Project Output
Output dari project ini adalah model machine learning yang dapat memprediksi harga tiket pesawat berdasarkan fitur-fitur tertentu.

## Data
[Data](https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction/data)
Dataset yang digunakan adalah Flight Price Prediction dari Kaggle, dataset ini sekitar 300.261 baris data pemesanan penerbangan. 

Data awalnya di-scrape dari situs “Ease My Trip” (platform pemesanan tiket penerbangan di India) dalam kurun waktu sekitar 50 hari (dari 11 Februari sampai 31 Maret 2022). 

Dataset ini terdiri dari sekitar 12 kolom fitur (termasuk fitur target yaitu harga tiket).

The various features of the cleaned dataset are explained below:
1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
10) Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
11) Price: Target variable stores information of the ticket price.

## Method
Model machine learning yang menggunakan metode - metode regresi seperti KNN, SVM, Decision Tree, Random Forest dan Gradient Boost.

## Stacks
Python, Pandas, numPy, Matplotlib, Seaborn, scikit-learn, sciPy, plotly-express, streamlit, Jupyter Notebook.

## Reference
https://indian-flights-price-prediction.streamlit.app/


---
