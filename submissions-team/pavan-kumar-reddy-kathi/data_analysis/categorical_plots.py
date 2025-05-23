import matplotlib.pyplot as plt

from dpputility.data_set_module import get_data_frame
import seaborn as sns

# Load dataset
dataset = get_data_frame()

# Count plot
sns.countplot(data=dataset, x='clarity')
plt.title('cut bar plot')
plt.show()

# Box Violin plots
sns.boxplot(data=dataset, x='cut', y='price')
sns.violinplot(data=dataset, x='cut', y='price')
plt.show()
