# Retail Sales Analysis and Visualization

## Project Journey
This project began as an exercise to analyze an online retail dataset (`Online_Retail.xlsx`) and prepare strategic questions for a hypothetical CEO and CMO, aiming to evaluate business performance and guide expansion. The journey evolved into a full-fledged data analysis and visualization project, where I used Python with `pandas` and `matplotlib` to create professional visuals: a bar chart of top-selling products and a table of revenue by country. This repository documents the entire process, from drafting business questions to overcoming technical challenges and producing polished outputs for sharing on GitHub and LinkedIn. The project reflects my learning path as an aspiring data analyst, building on my technical background in Computer Science and experience with tools like Python and Tableau.

### Phase 1: Drafting Business Questions
The initial goal was to analyze the retail dataset to prepare for a strategic meeting with business leaders. I used the dataset’s columns—`InvoiceNo`, `StockCode`, `Description`, `Quantity`, `InvoiceDate`, `UnitPrice`, `CustomerID`, and `Country—to formulate questions that would uncover insights into revenue drivers, customer behavior, and operational efficiency. The questions were tailored to the CEO’s focus on growth and the CMO’s interest in marketing optimization.

**CEO Questions**:
1. What are the key drivers of revenue growth across product categories, and how do they correlate with customer demographics (e.g., country, purchase frequency)?
2. How does average order value (AOV) vary by country, and what operational factors (e.g., shipping costs, product mix) influence these variations?
3. What is the trend in customer retention and repeat purchase rates, and how does this impact long-term revenue sustainability?
4. Which regions show the highest revenue contribution, and what operational challenges (e.g., cancellations, discounts) hinder scaling these markets?

**CMO Questions**:
1. Which products have the highest sales volume and revenue, and how can we tailor marketing campaigns to promote them to similar customer segments?
2. How does purchasing behavior vary by country, and what cultural or seasonal marketing strategies can boost engagement in key markets?
3. What is the impact of discounts and cancellations on customer acquisition and retention, and how can we optimize promotional strategies?
4. Which customer segments (based on purchase frequency, spend, or product preferences) are most responsive to marketing efforts, and how can we refine messaging?

**Thought Process**: The questions were designed to align with the dataset’s structure, leveraging metrics like revenue (`Quantity * UnitPrice`), geographic segmentation (`Country`), and customer loyalty (`CustomerID`). I aimed to provide actionable insights for strategic planning and marketing, reflecting my understanding of business needs.

### Phase 2: Transition to Visualization
To showcase my analysis skills on LinkedIn, I decided to visualize key insights from the dataset, focusing on top-selling products and revenue by country. I chose Python with `pandas` for data processing and `matplotlib` for visualization, inspired by my prior experience with data projects (e.g., an ESG analytics dashboard). The goal was to create professional, McKinsey-style visuals that would appeal to my professional network and demonstrate my technical and analytical abilities.

### Phase 3: Technical Challenges
The journey wasn’t without hurdles. Initially, I faced an `openpyxl` import error when loading the Excel file, as `pandas.read_excel` required this library. I resolved this by installing `openpyxl` with `pip install openpyxl`. Another issue arose when I tried running Python code directly in PowerShell, resulting in a “df not recognized” error. This was because I mistakenly executed script lines in the shell instead of within a Python environment. I learned to run the script correctly using `python retail_visuals.py` and verified the Excel filename (`Online_Retail.xlsx` vs. `Online Retail.xlsx`). These challenges taught me the importance of environment setup and precise file handling, skills I’ll carry forward in future projects.

## Project Overview
The final project analyzes the online retail dataset to identify top-selling products and revenue distribution by country, producing two visuals: a bar chart of the top 5 products by revenue and a table of revenue by country. These outputs were designed to support the strategic questions posed earlier, providing clear insights for business leaders. The project showcases my ability to clean, analyze, and visualize data using Python, with a focus on professional presentation for sharing on GitHub and LinkedIn.

## Dataset
The dataset, `Online_Retail.xlsx`, contains transactional data from a UK-based online retailer (December 2010–December 2011). Key columns include:
- `InvoiceNo`: Transaction ID (cancellations start with 'C').
- `StockCode`: Product code.
- `Description`: Product name.
- `Quantity`: Items purchased.
- `InvoiceDate`: Transaction date.
- `UnitPrice`: Price per item.
- `CustomerID`: Customer identifier.
- `Country`: Customer’s country.

The dataset’s structure enabled analysis of sales performance, customer segmentation, and geographic trends, making it ideal for business insights.

## Thought Process
My approach was driven by the following considerations:
1. **Business Alignment**: The visuals needed to address the CEO’s focus on revenue growth and the CMO’s need for marketing insights, building on the initial questions.
2. **Data Integrity**: Retail datasets often have issues like cancellations or missing values. Thorough cleaning ensured accurate results.
3. **Metric Selection**: Revenue (`Quantity * UnitPrice`) was the core metric, with product and country groupings to highlight key drivers.
4. **Visualization Design**: I chose a bar chart for products (to emphasize top performers) and a table for countries (to summarize geographic data concisely). Visuals needed to be clear, professional, and McKinsey-inspired (navy/gold color scheme, no overlapping labels).
5. **Learning Showcase**: As part of my data analyst journey, I aimed to produce outputs that demonstrate technical skills and business acumen to my LinkedIn network.

## Methodology
The analysis was implemented in Python using `pandas` and `matplotlib`. Below are the steps:

### 1. Data Loading and Cleaning
- **Loading**: Loaded `Online_Retail.xlsx` with `pandas.read_excel`, requiring `openpyxl`.
- **Cleaning**:
  - Removed cancellations (`InvoiceNo` starting with 'C') to focus on valid sales.
  - Filtered out records with negative `Quantity`, zero/negative `UnitPrice`, or missing `CustomerID`.
- **Rationale**: Clean data was essential for accurate revenue calculations and reliable insights.

### 2. Revenue Calculation
- Created a `Revenue` column (`Quantity * UnitPrice`) for analysis.
- **Rationale**: Revenue is a direct indicator of business performance, central to both visuals.

### 3. Bar Chart: Top 5 Products by Revenue
- **Analysis**: Grouped by `Description`, summed `Revenue`, and selected the top 5 using `sort_values` and `head(5)`.
- **Visualization**:
  - Plotted a bar chart with `matplotlib.pyplot.bar`.
  - Used navy blue (`#003087`) bars and gold (`#FFD700`) value labels for a professional look.
  - Added £-formatted labels above bars for clarity.
  - Rotated x-axis labels 45 degrees and used `tight_layout` to avoid overlap.
- **Output**: Saved as `top_products.png` (300 DPI).
- **Rationale**: A bar chart highlights top products, aiding marketing prioritization.

### 4. Table: Revenue by Country
- **Analysis**: Grouped by `Country`, summed `Revenue`, and calculated `% of Total` for the top 5.
- **Visualization**:
  - Created a table with `matplotlib.pyplot.table` (`Country`, `Revenue (£)`, `% of Total`).
  - Styled with navy headers, white header text, and alternating row colors (`#F5F6F5`/white).
  - Hid axes and added a bold title for focus.
- **Output**: Saved as `country_revenue_table.png` (300 DPI).
- **Rationale**: A table summarizes geographic contributions, supporting expansion decisions.

### 5. Design Choices
- **Colors**: Navy and gold for a sophisticated, business-friendly aesthetic.
- **Clarity**: Ensured no label overlap and used high-resolution outputs.
- **Portability**: PNG format for easy sharing on GitHub/LinkedIn.
- **Rationale**: Professional visuals enhance credibility and appeal to stakeholders.

## Code Structure
The script (`retail_visuals.py`) is structured as:
- **Imports**: `pandas`, `matplotlib.pyplot`, `numpy`.
- **Data Loading/Cleaning**: Loads and filters the dataset.
- **Revenue Calculation**: Computes `Revenue`.
- **Bar Chart**: Groups data, plots, and saves the chart.
- **Table**: Formats and saves the country revenue table.
- **Output**: Confirms file creation.

The code is modular and reusable, with comments for clarity.

## Outputs
The script produces:
1. **`top_products.png`**: Bar chart of top 5 products by revenue (e.g., "WHITE HANGING HEART T-LIGHT HOLDER"), navy bars, gold labels.
2. **`country_revenue_table.png`**: Table of top 5 countries (e.g., United Kingdom), with revenue and percentage, navy headers, alternating rows.

View them here:
- [Top Products Bar Chart](top_products.png)
- [Country Revenue Table](country_revenue_table.png)

## Setup and Running
### Prerequisites
- Python 3.8+
- Libraries: `pandas`, `matplotlib`, `numpy`, `openpyxl`
- Dataset: `Online_Retail.xlsx`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/retail-sales-analysis.git
   cd retail-sales-analysis
   ```
2. Install dependencies:
   ```bash
   pip install pandas matplotlib numpy openpyxl
   ```
3. Place `Online_Retail.xlsx` in the project directory.

### Running
1. Execute:
   ```bash
   python retail_visuals.py
   ```
2. Outputs: `top_products.png`, `country_revenue_table.png`, and a confirmation message.

## Challenges and Solutions
- **Openpyxl Error**: Resolved by installing `openpyxl` (`pip install openpyxl`).
- **PowerShell Error**: Mistakenly ran Python code in PowerShell. Fixed by running the script via `python retail_visuals.py`.
- **Filename Mismatch**: Ensured the Excel filename matched the script (`Online_Retail.xlsx`).
- **Label Overlap**: Used `plt.tight_layout` and rotated labels to ensure clarity.

## Future Improvements
- **Interactive Visuals**: Use `plotly` for hoverable charts.
- **Extended Analysis**: Explore customer retention or seasonal trends with `InvoiceDate`.
- **Tableau Integration**: Create complementary Tableau dashboards, as explored earlier.
- **Automation**: Script dynamic analysis for different time periods or categories.

## Motivation
This project was a milestone in my transition to a data analyst role, building on my Computer Science background and experience with Python and Tableau (e.g., past ESG dashboard project). It demonstrates my ability to analyze real-world data, overcome technical challenges, and present insights professionally. Sharing this on GitHub and LinkedIn connects me with the data analytics community and showcases my growth.

## License
MIT License. See [LICENSE](LICENSE).

## Acknowledgments
- Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail).
- Inspired by my goal to excel in data analytics and share my journey.

Explore the code and visuals, and feel free to provide feedback!