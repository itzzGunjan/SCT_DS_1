import matplotlib.pyplot as plt
import numpy as np


ages = [25, 30, 22, 28, 35, 40, 42, 38, 27, 29]


gender = ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
gender_encoded = [0 if g == 'Male' else 1 for g in gender]


plt.hist(ages, bins=5, edgecolor='none')  


colors_for_ages = ['red', 'green', 'blue', 'yellow', 'purple']
for i, patch in enumerate(plt.gca().patches):
    patch.set_facecolor(colors_for_ages[i]) 

plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')
plt.show()


plt.hist(gender_encoded, bins=[-0.5, 0.5, 1.5], align='mid', rwidth=0.8, edgecolor='none')  


colors_for_gender = ['blue', 'pink']
for i, patch in enumerate(plt.gca().patches):
    patch.set_facecolor(colors_for_gender[i]) 

plt.xticks([0, 1], ['Male', 'Female'])
plt.xlabel('Gender')
plt.ylabel('Frequency')
plt.title('Gender Distribution')
plt.show()
