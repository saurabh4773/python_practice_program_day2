''' in this program student.csv file read using python pandas and 
then using matplotlib plot the graph bar '''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student.csv")
#print(df)

plt.figure(figsize=(10,5))
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.bar(df['name'], df['marks'])
plt.show()