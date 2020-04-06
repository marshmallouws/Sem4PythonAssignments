import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
import numpy as np

# load 'iris_data.csv' into a dataframe
df = pd.read_csv("iris_data.csv")

# get unique labels (Species column)
species = df["Species"].unique()

# plot with a scatter plot each iris flower sample colored by label (3 different colors)
# Making two different plots for petals and sepals
fig_sepal = plt.figure()
fig_petal = plt.figure()
ax1 = fig_sepal.add_subplot(111)
ax2 = fig_petal.add_subplot(111)

colors = ["r", "b", "g"]

for spec, color in zip(species, colors):
    s = df[df["Species"] == spec]

    x1 = s["Sepal length"]
    y1 = s["Sepal width"]
    ax1.scatter(x1, y1, c=color, linewidth=0.2)

    x2 = s["Petal length"]
    y2 = s["Petal width"]
    ax2.scatter(x2, y2, c=color, linewidth=0.2)
plt.show()

# use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate
# bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an
# argument: quantile set it to 0.2 for best result
sepal_data = df[["Sepal length", "Sepal width"]]
petal_data = df[["Petal length", "Petal width"]]

s_bandwidth = estimate_bandwidth(sepal_data, quantile=0.2)
p_bandwidth = estimate_bandwidth(petal_data, quantile=0.2)

pms = MeanShift(bandwidth=p_bandwidth, bin_seeding=True)
pms.fit(petal_data)  # Perform clustering
clusters = pms.cluster_centers_  # Find centers
no_clusters = len(clusters)  # Number of clusters
labels = pms.labels_

# print out labels, cluster centers and number of clusters
# (as returned from the MeanShift function
print(no_clusters)
print(clusters)
print(labels)

# create a new scatter plot where each flower is colored according to cluster label
# add a dot for the cluster centers

fig_petal_cluster = plt.figure()
ax = fig_petal_cluster.add_subplot(111)
c = ["r", "b", "g", "y"]
for clust, col in zip(range(len(clusters)), c):
    center = clusters[clust]
    my_members = labels == clust

    p = petal_data.to_numpy()
    x, y = p[my_members, 0], p[my_members, 1]
    ax.scatter(x, y, c=col, linewidth=0.2)
    ax.scatter(center[0], center[1], c="k", s=50)

plt.xticks(np.arange(0, 9, step=1))
plt.yticks(np.arange(0, 4, step=0.5))
plt.show()


# Compare the 2 plots (colored by actual labels vs. colored by cluster label)

for test in range(no_clusters):
    
