🧩 Clustering and PCA Visualization
📘 Project Overview

This part of the project focuses on unsupervised learning, specifically applying K-Means Clustering and Principal Component Analysis (PCA) to explore hidden patterns and groupings within the dataset.
Unlike regression or classification models, clustering does not rely on labeled outputs — instead, it identifies natural structures based on data similarities.

🎯 Objective

Implement K-Means Clustering to automatically group similar data points.

Apply PCA (Principal Component Analysis) to reduce data dimensionality for better visualization.

Visualize and interpret cluster patterns in 2D space using PCA-transformed data.

Derive insights about the natural distribution and relationships within the dataset.

⚙️ Steps Performed
🔹 Step 1: Data Loading and Preparation

Imported the dataset using pandas.

Selected relevant numerical features for clustering.

Handled missing values by filling them with median or mean values.

Scaled the features using StandardScaler to ensure that all variables contribute equally to distance calculations.

🔹 Step 2: Principal Component Analysis (PCA)

Applied PCA to reduce the number of features into two principal components.

These components capture the maximum variance of the dataset while minimizing information loss.

The transformed data enables clear 2D visualization.

🔹 Step 3: K-Means Clustering

Applied the K-Means algorithm to identify natural clusters in the data.

Determined the optimal number of clusters (K) using the Elbow Method by plotting the Within-Cluster Sum of Squares (WCSS).

Once the best value of K was selected, the K-Means model was fitted to the data, and each observation was assigned to a cluster.

🔹 Step 4: Visualization in 2D

Visualized the clustered data in a 2D scatter plot using PCA results.

Each cluster was represented with a different color for clarity.

The cluster centroids were marked on the plot to show the central point of each group.

📊 Results and Insights
Feature	Description
PCA1, PCA2	The two principal components representing the reduced-dimensional space.
Clusters (0, 1, 2, ...)	Groups of data points formed based on feature similarity.
Centroids	The mean positions of all the points in each cluster, representing cluster centers.
✅ Key Findings

The data formed distinct clusters, indicating clear separations between different groups of observations.

PCA effectively captured the variance and provided a clear 2D representation.

K-Means efficiently grouped similar observations, supporting deeper data-driven insights.

Visualization showed that some clusters are well-separated, while others have partial overlap — implying moderate feature correlation.

🧠 Interpretation

The combination of K-Means and PCA provided meaningful insights into the dataset’s structure:

Each cluster may represent a distinct customer segment, behavior pattern, or category within the data.

PCA helped simplify the dataset without significant information loss, making it easier to interpret and visualize.

Clustering outcomes can be used to support targeted marketing, recommendation systems, or data segmentation strategies.

📈 Visualizations Included

Elbow Curve (WCSS vs. K) – To determine the optimal number of clusters.

2D PCA Scatter Plot – To visualize cluster distribution in reduced dimensions.

Cluster Centroids Marked – To highlight the center of each cluster visually.

🧩 Evaluation

While unsupervised models do not use accuracy as a metric, evaluation was performed by:

Checking cluster compactness (data points within clusters should be close together).

Assessing cluster separation (clusters should be distinct from each other).

Optionally using Silhouette Score to measure overall clustering quality.

🏁 Project Milestone: Add Unsupervised Analysis

✅ Applied K-Means Clustering to detect natural data groupings.
✅ Reduced high-dimensional data to 2D using PCA for visualization.
✅ Created clear visual insights into the structure of the dataset.
✅ Successfully integrated unsupervised learning into the overall project pipeline.

💡 Reflection

This milestone expanded the project’s analytical depth by introducing unsupervised learning, allowing for exploration beyond labeled outcomes.
The clustering and PCA visualization revealed data patterns that were not visible through regression or classification alone — making this a crucial step in achieving a well-rounded data analysis pipeline.

---

### 👩‍💻 Author
**Maliha Khokhar**  
*AI & DS Assignment — Customer Churn Prediction Project*  
*Semester: BS Software Engineering*  