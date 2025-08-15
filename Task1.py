import matplotlib.pyplot as plt
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate sample age data (150 individuals between 18 and 70)
ages = np.random.randint(18, 70, size=150)

# Create bins for bar chart (grouping ages)
age_bins = [18, 25, 30, 35, 40, 45, 50, 60, 70]
age_labels = ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-59', '60-69']
age_counts = np.histogram(ages, bins=age_bins)[0]

# Create bar chart (age groups)
plt.figure(figsize=(10, 4))
plt.bar(age_labels, age_counts, color='skyblue', edgecolor='black')
plt.title('Bar Chart: Distribution of Age Groups')
plt.xlabel('Age Group')
plt.ylabel('Number of Individuals')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Create histogram (exact ages)
plt.figure(figsize=(10, 4))
plt.hist(ages, bins=10, color='salmon', edgecolor='black')
plt.title('Histogram: Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
