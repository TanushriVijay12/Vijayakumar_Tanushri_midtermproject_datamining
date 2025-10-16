# Association Rule Mining

## Overview
This project explores **Association Rule Mining** by implementing and comparing three different approaches:

1. **Brute Force** 
2. **Apriori** (using the `mlxtend` library)  
3. **FP-Growth** (using the `mlxtend` library)  

The goal is to extract **frequent itemsets** and **association rules** from transaction datasets, then compare the efficiency of the algorithms.

---

## ⚙️ Setup & Installation

1. Clone the repository
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
2. Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
3. Install dependencies

---

## Steps to Run

### Option 1  - Jupyter Notebook

    jupyter notebook

- Open notebooks/midterm_project.ipynb
- Select a dataset when prompted
- Enter minimum support and confidence values
- View frequent itemsets, rules, and execution time comparison

### Option 2 - Python scripts

Run individual algorithms:
- python src/brute_force.py
- python src/apriori.py
- python src/fpgrowth.py

