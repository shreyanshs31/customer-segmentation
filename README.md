# Customer Segmentation

A machine learning project that segments mall customers into distinct groups based on their annual income, spending behavior, and age using the K-Means clustering algorithm.

## Table of Contents

- [What It Does](#what-it-does)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## What It Does

This project analyzes customer data from a shopping mall and automatically segments customers into meaningful groups using K-Means clustering. By identifying customer segments based on income levels and spending patterns, retailers can tailor marketing strategies, product offerings, and customer engagement for each segment.

The analysis considers three key features:
- **Annual Income** (in thousands of dollars)
- **Spending Score** (1-100 scale based on customer behavior and spending nature)
- **Age** (customer age in years)

## Key Features

- **Data Preprocessing**: Standardizes features for optimal clustering performance
- **Elbow Method Analysis**: Determines the optimal number of clusters through WCSS (Within-Cluster Sum of Squares) visualization
- **K-Means Clustering**: Groups customers into distinct segments with optimal centroid initialization
- **Data Visualization**: Generates comprehensive visualizations including:
  - Distribution histograms for age, income, and spending scores
  - Correlation heatmap of customer features
  - Scatter plots revealing customer segments
  - Elbow method chart for cluster optimization
- **Easy Integration**: Simple Python script that can be extended for additional analysis

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shreyanshs31/customer-segmentation.git
   cd customer-segmentation
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install pandas matplotlib seaborn scikit-learn
   ```

### Running the Project

Execute the main script:

```bash
python customerSegmentation.py
```

The script will:
1. Load the customer data from `Mall_Customers.csv`
2. Preprocess and standardize the features
3. Apply K-Means clustering (k=5 clusters)
4. Generate a visualization of customer segments

The output will display a scatter plot showing how customers are distributed across the identified segments based on annual income and spending score.

## Dataset

The project uses `Mall_Customers.csv` containing 200 customer records with the following columns:

- **CustomerID**: Unique customer identifier
- **Gender**: Customer gender (Male/Female)
- **Age**: Customer age in years
- **Annual Income (k$)**: Annual income in thousands of dollars
- **Spending Score (1-100)**: Spending score assigned based on customer behavior and purchasing patterns

### Data Statistics

- **Total Records**: 200 customers
- **Age Range**: 18-70 years
- **Income Range**: $15k-$137k
- **Spending Score Range**: 1-99 (normalized to 1-100)

## Project Structure

```
customer-segmentation/
├── customerSegmentation.py      # Main clustering script
├── Mall_Customers.csv           # Customer dataset
├── README.md                    # This file
├── ageHistogram.png             # Age distribution visualization
├── annualIncomeHistogram.png    # Income distribution visualization
├── spendingScoreHistogram.png   # Spending score distribution
├── correlation_heatmap.png      # Feature correlation matrix
├── scatterAnnualIncomevsSpendingScore.png  # Raw data visualization
├── elbow_method.png             # Elbow curve for cluster optimization
└── cluster_map.png              # Customer segments visualization
```

## How It Works

### Algorithm Overview

1. **Data Loading**: Reads customer data from the CSV file
2. **Feature Selection**: Selects Annual Income, Spending Score, and Age
3. **Standardization**: Applies StandardScaler to normalize features (zero mean, unit variance)
4. **Optimal Clusters**: Uses the Elbow Method to determine the best number of clusters
5. **Clustering**: Applies K-Means algorithm with k=5 clusters
6. **Visualization**: Plots results to identify customer segments

### Elbow Method

The Elbow Method identifies the optimal number of clusters by plotting WCSS against the number of clusters. The "elbow" point (where WCSS decreases at a slower rate) indicates the optimal cluster count.

### K-Means Algorithm

K-Means divides customers into k clusters by:
- Initializing k random centroids
- Assigning each customer to the nearest centroid
- Recalculating centroids based on cluster members
- Iterating until convergence

## Results

The clustering analysis reveals **5 distinct customer segments**:

1. **Low Income, Low Spending**: Budget-conscious customers
2. **High Income, Low Spending**: Potential high-value customers
3. **Mid Income, Mid Spending**: Average customers
4. **Mid Income, High Spending**: Regular shoppers
5. **High Income, High Spending**: Premium customers

These segments enable targeted marketing strategies for different customer groups.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

Please ensure your code follows Python best practices and includes appropriate comments.

## License

This project is open source and available under the MIT License. See the LICENSE file for more details.

## Support

For questions, issues, or suggestions, please open an issue on the GitHub repository. Check existing issues first to avoid duplicates.

---

**Author**: Shreyansh Shukla  
**Repository**: [github.com/shreyanshs31/customer-segmentation](https://github.com/shreyanshs31/customer-segmentation)
