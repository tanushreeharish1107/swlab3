import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
tips = sns.load_dataset("tips")

# 1) Heatmap
ax = sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm")
ax.figure.savefig("heatmap_tips.png", bbox_inches="tight")
plt.close()

# 2) Histogram of total_bill
tips["total_bill"].hist(bins=20).figure.savefig("hist_total_bill.png", bbox_inches="tight")
plt.close()

# 3) Scatter plot: total_bill vs tip by sex
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex").figure.savefig("scatter_tb_tip.png", bbox_inches="tight")
plt.close()

# 4) Cleaning on a copy
tips_copy = tips.copy()
before = tips_copy.shape
tips_copy = tips_copy.drop_duplicates().drop(columns=["size"])
after = tips_copy.shape

with open("cleaning_summary.txt", "w") as f:
    f.write(f"Original shape: {tips.shape}\n")
    f.write(f"Copied before: {before}\n")
    f.write(f"Copied after:  {after}\n")
