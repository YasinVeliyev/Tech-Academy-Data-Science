import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import sys

df = pd.read_csv("k-means.csv")
data = df.copy()

pattern = re.compile("\D+")

data.columns = [0, 1, 2]
data[1] = data[1].apply(lambda x: int(re.sub(pattern, "", x)))

for i in data.columns:
    data[i] = (data[i]-data[i].min())/(data[i].max()-data[i].min())

def k_means(df,k,centroids):
    
    for i in range(20):
        scaleCentroid = [[] for _ in range(k)]
        for coordinates in df.values:
            distance=[]
            for centroid in centroids:
                distance.append(np.sqrt(np.sum((coordinates-centroid)**2)))
                # with open("log.txt","a") as f:
                #     f.write(f"Centroid: {centroid},\nCoordinates:{coordinates}, \nDistance:{(coordinates-centroid)**2} ,\nSum of Distance:{np.sqrt(np.sum((coordinates-centroid)**2))}\n\n\n")
            dmin=np.argmin(distance)
                
            scaleCentroid[dmin].append(coordinates)
        for i in range(k):
            # with open("log_a.txt","a") as f:
            #     f.write(f"Distance: {distance},\nDmin: {dmin},\nCentroid:{centroids[i]},\nCoordinates: {scaleCentroid[i]},\nAverage:{np.average(scaleCentroid[i],axis=0)}\n\n\n")
            if np.isnan(np.average(scaleCentroid[i],axis=0)).all():
                continue
            centroids[i] = np.average(scaleCentroid[i],axis=0)
    return centroids,scaleCentroid


k = 3

centroids = np.array([[0.2, 1], [0.15, 0.2], [1, 1]])
centroids, scaleCentroid = k_means(data.iloc[:, 1:], k, centroids)

def visualize(k,centroids,scaleCentroid):
    clusterX=[[] for _ in range(k)]
    clusterY=[[] for _ in range(k)]
    for i in range(k):
        for j in range(len(scaleCentroid[i])):
            clusterX[i].append(scaleCentroid[i][j][0])
            clusterY[i].append(scaleCentroid[i][j][1])
    fig,ax=plt.subplots()
    ax.set_title(f"k={k}")
    for i in range(k):
        ax.scatter(clusterX[i],clusterY[i],color=f"C{i}")
    for centroid in centroids:
            ax.plot(centroid[0],centroid[1],marker="x",color="black",alpha=0.7)
    fig.show()    
visualize(k,centroids,scaleCentroid)



def elbow_method(K,Centroids):
    wcss=[]
    for k in range(1,K):
        Centroids=Centroids.copy()
        centroids,scaleCentroid=k_means(data.iloc[:,1:],k,Centroids[:k])
        s=0
        for c in range(len(centroids)):
            for j in range(len(scaleCentroid[c])):
                d=0
                for coordinat in scaleCentroid[c][j]:
                    d+=np.sqrt(np.sum((coordinat-centroids[c])**2))
                s+=d
        wcss.append(s)
        visualize(k,centroids,scaleCentroid)
    fig,ax=plt.subplots()
    ax.plot(range(1,K),wcss)
Centroids = np.array([[0.2,1],[0.15,0.2],[1,1],[0.2,0.6],[0.1,0.8],[0.4,0.1],[1,0.1],[0.1,0.9],[0.1,0.3]])
# elbow_method(10,Centroids)

k=6
Centroids = np.array([[0.2,1],[0.15,0.2],[1,1],[0.2,0.6],[0.1,0.8],[0.4,0.1],[1,0.1],[0.1,0.9],[0.1,0.3]])

fig,ax=plt.subplots()
ax.scatter(data.iloc[:,1],data.iloc[:,2])

for centroid in Centroids:
    ax.plot(centroid[0],centroid[1],marker="x",color="red",alpha=0.7)
fig.show()

centroids=Centroids.copy()
centroids,scaleCentroid=k_means(data.iloc[:,1:],k,centroids[:k])
