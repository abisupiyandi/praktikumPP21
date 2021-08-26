#Import Data (loading data in Python: csv, text, XML, image)
#Buat file dengan header, misalkan terdiri dari Nama Pasien, Umur, Penyakit, Gender seperti pada tabel berikut dan simpan kedalam format CSV dan Text (Tab delimeter)
#data disimpan dalam folder data/
import pandas as pd

# Membaca data dari file dengan format CSV
data = pd.read_csv("./data/data.csv", sep=";")
print(data)

#Membaca data dari file dengan format text (delimeter)
print("\n read text data with tab delimiter")
with open ('./data/data.txt') as data:
print(data.read())  

import pandas as pd
f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)
