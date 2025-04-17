import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_excel('Online_Retail.xlsx')

# Data cleaning
# Remove cancellations (InvoiceNo starting with 'C') and invalid records
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
df = df.dropna(subset=['CustomerID'])

# Calculate revenue
df['Revenue'] = df['Quantity'] * df['UnitPrice']

# --- Bar Chart: Top 5 Products by Revenue ---
# Group by product description and sum revenue
product_revenue = df.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(5)

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(product_revenue.index, product_revenue.values, color='#003087')  # Navy blue
plt.title('Top 5 Revenue-Generating Products', fontsize=14, weight='bold', color='#003087')
plt.xlabel('Product', fontsize=12, color='#003087')
plt.ylabel('Revenue (£)', fontsize=12, color='#003087')
plt.xticks(rotation=45, ha='right', fontsize=10, color='#003087')
plt.yticks(fontsize=10, color='#003087')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02*yval, f'£{yval:,.2f}', 
             ha='center', va='bottom', fontsize=10, color='#FFD700')  # Gold labels

plt.tight_layout()  # Prevent overlapping
plt.savefig('top_products.png', dpi=300, bbox_inches='tight')
plt.close()

# --- Table: Revenue by Country ---
# Group by country and sum revenue
country_revenue = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False).head(5)
country_revenue = country_revenue.reset_index()
country_revenue['Revenue (£)'] = country_revenue['Revenue'].apply(lambda x: f'£{x:,.2f}')
country_revenue['% of Total'] = (country_revenue['Revenue'] / country_revenue['Revenue'].sum() * 100).apply(lambda x: f'{x:.1f}%')
country_revenue = country_revenue[['Country', 'Revenue (£)', '% of Total']]

# Create figure for table
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('off')  # Hide axes

# Create table
table = ax.table(cellText=country_revenue.values,
                 colLabels=country_revenue.columns,
                 loc='center',
                 cellLoc='center',
                 colColours=['#003087']*3,  # Navy blue headers
                 colWidths=[0.4, 0.3, 0.3])

# Style table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
for (i, j), cell in table.get_celld().items():
    if i == 0:
        cell.set_text_props(color='white', weight='bold')  # White text for headers
    else:
        cell.set_text_props(color='#003087')  # Navy text for data
        cell.set_facecolor('#F5F6F5' if i % 2 == 0 else 'white')  # Alternating row colors

plt.title('Revenue by Country', fontsize=14, weight='bold', color='#003087', pad=20)
plt.savefig('country_revenue_table.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visuals saved as 'top_products.png' and 'country_revenue_table.png'")
