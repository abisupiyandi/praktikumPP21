#Import Data (loading data in Python: csv, text, XML, image)
#Buat file dengan header, misalkan terdiri dari Nama Pasien, Umur, Penyakit, Gender seperti pada tabel berikut dan simpan kedalam format CSV dan Text (Tab delimeter)
#data disimpan dalam folder data/
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Membaca data dari file dengan format CSV
data = pd.read_csv("./data/data.csv", sep=";")
print(data)

#Membaca data dari file dengan format text (delimeter)
print("\n read text data with tab delimiter")
with open ('./data/data.txt') as data:
print(data.read())  

f = pd.read_csv('http://www.exploredata.net/ftp/Spellman.csv')
print(f)


#Membaca file dan menyajikan dalam bentuk grafik. 
traffic = sp.genfromtxt("web_traffic.tsv",delimiter='\t')
print(traffic[:10])
print(traffic.shape)

x = traffic[:,0]
y = traffic[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y)
plt.title("Web traffic last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")

plt.xticks([w*7*24 for w in range(10)],['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()
