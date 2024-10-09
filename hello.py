# Program to plot 2-D Heat map 
# using matplotlib.pyplot.imshow() method 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

# create figure
fig = plt.figure(figsize=(5, 5))
rows = 1
columns = 2

dfh = pd.read_csv("dataAdultHorizontal.csv")
dfv = pd.read_csv("dataAdultVertical.csv")
dfc = pd.read_csv("adultCentralized.csv")

#Quitar si no se quiere el horizontal y vertical en la misma imagen
#fig.add_subplot(rows, columns, 1)

plt.imshow(dfh, cmap='Reds', interpolation='nearest')
plt.colorbar()

plt.xticks(np.arange(8), [50, 150, 200, 250, 400, 600,1000,2000])
plt.yticks(np.arange(4), [0.01, 0.1, 0.5, 1])
plt.xlabel("Microaggregation k")
plt.ylabel("Privacy budget ϵ")
plt.title( "Horizontally fragmented data" )

plt.show()

#Quitar si no se quiere el horizontal y vertical en la misma imagen
#fig.add_subplot(rows, columns, 2)
plt.imshow(dfv, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(np.arange(8), [50, 150, 200, 250, 400, 600,1000,2000])
plt.yticks(np.arange(4), [0.01, 0.1, 0.5, 1])
plt.xlabel("Microaggregation k")
plt.ylabel("Privacy budget ϵ")
plt.title( "Vertically fragmented data" )


ax = plt.gca()

plt.show()

# plot a line graph
fig, ax = plt2.subplots()
# Using matshow here just because it sets the ticks up nicely. imshow is faster.
ax.matshow(dfc, cmap='Reds', interpolation='nearest')
ax.tick_params(top=False, labeltop=False, bottom=True, labelbottom=True)
for (i, j), z in np.ndenumerate(dfc):
    ax.text(j, i, '{:0.1f}'.format(z))

plt2.xticks(np.arange(8), [50, 150, 200, 250, 400, 600,1000,2000])
plt2.yticks(np.arange(4), [0.01, 0.1, 0.5, 1])
plt2.xlabel("Microaggregation k")
plt2.ylabel("Privacy budget ϵ")
plt2.title( "Centralized iDP-IR" )

plt2.show()
