import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('Mall_Customers.csv')
# print(df.describe())
# print(df.info())

#*****Univariate Analysis*********
# plt.figure(figsize=(10,6))
# plt.hist(x=df['Age'], bins=20, color='skyblue', edgecolor='black')
# plt.title('Distribution of Age')
# plt.xlabel('age')
# plt.ylabel('Frequency')
# plt.savefig('ageHistogram.png')

#*****Univariate Analysis*********
# plt.hist(x=df['Annual Income (k$)'], bins=20, color='skyblue', edgecolor='black')
# plt.title('Distribution of Annual Income')
# plt.xlabel('Income')
# plt.ylabel('Frequency')
# plt.savefig('annualIncomeHistogram.png')

#*****Univariate Analysis*********
# plt.hist(x=df['Spending Score (1-100)'], bins=20, color='skyblue', edgecolor='black')
# plt.title('Distribution of Spending Score')
# plt.xlabel('Spending Score')
# plt.ylabel('Frequency')
# plt.savefig('spendingScoreHistogram.png')

#*****Univariate Analysis*********
# plt.hist(x=df['Gender'], bins=2, color='skyblue', edgecolor='black')
# plt.title('Distribution of Gender')
# plt.xlabel('Gender')
# plt.ylabel('Frequency')
# plt.savefig('genderHistogram.png')

#*****Bivariate Analysis*********
# plt.scatter(x=df['Annual Income (k$)'], y=df['Spending Score (1-100)'], color='skyblue', edgecolors='black')
# plt.title('Scatter plot')
# plt.xlabel('Annual Income')
# plt.ylabel('Spending Score')
# plt.savefig('scatterAnnualIncomevsSpendingScore')

#*******Heatmap********
# numeric_df= df.select_dtypes(include=['number'])
# corr_matrix = numeric_df.corr()
# plt.figure(figsize=(10,8))
# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
# plt.title('Correlation Matrix of Customer Features')
# plt.savefig('correlation_heatmap.png')


#************Feature Selection two variables*************
# with Annual Income and Spending Score

# X=df[['Annual Income (k$)', 'Spending Score (1-100)']]
# scaler = StandardScaler()
# X_scaled=scaler.fit_transform(X)
# print(X_scaled[:5])

#***********Feature Selection three variables*************
# with Annual Income, Spending Score and Age

X=df[['Annual Income (k$)', 'Spending Score (1-100)', 'Age']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
# print(X_scaled[:5])

#******* Elbo Method**********
# wcss = []
# for i in range(1, 11):
#     kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
#     kmeans.fit(X_scaled)
#     wcss.append(kmeans.inertia_)

# plt.figure(figsize=(10, 6))
# plt.plot(range(1, 11), wcss, marker='o')
# plt.title('The Elbow Method')
# plt.xlabel('Number of Clusters')
# plt.ylabel('WCSS Score')
# plt.savefig('elbow_methodTheeFeatureSelection.png')


kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
cluster_labels = kmeans.fit_predict(X_scaled)
# print(cluster_labels)

df['Cluster'] = cluster_labels
# print(df.head())

#*******2D figure plot*******
# plt.figure(figsize=(10, 6))
# sns.scatterplot(data=df, x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', palette='viridis', s=100)
# plt.title('Customer Segments')
# plt.xlabel('Annual Income')
# plt.ylabel('Spending Score')
# plt.legend(title='Cluster')
# plt.savefig('cluster_map.png')

#*******3D figure plot*******
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
xs = df['Age']
ys = df['Annual Income (k$)']
zs = df['Spending Score (1-100)']
scatter = ax.scatter(xs, ys, zs, c=df['Cluster'], cmap='viridis', s=50) # type: ignore
ax.set_xlabel('Age')
ax.set_ylabel('Annual Income')
ax.set_zlabel('Spending Score')
legend1 = ax.legend(*scatter.legend_elements(), title="Cluster")
ax.add_artist(legend1)
plt.title('3D Customer Segmentation')
plt.savefig('3d_cluster_map.png')

