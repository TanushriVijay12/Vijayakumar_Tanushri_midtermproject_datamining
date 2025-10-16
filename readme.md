# Association Rule Mining

## Overview
This project explores **Association Rule Mining** by implementing and comparing three different approaches:

1. **Brute Force**
2. **Apriori** (using the `mlxtend` library)
3. **FP-Growth** (using the `mlxtend` library)

The goal is to extract **frequent itemsets** and **association rules** from transaction datasets, then compare the efficiency of the algorithms.

---

## Setup & Installations

1. Clone the repository
    ```bash
   git clone https://github.com/TanushriVijay12/Vijayakumar_Tanushri_midtermproject_datamining.git
   cd Vijayakumar_Tanushri_midtermproject_datamining
    ```
2. Create and activate a virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```
3. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

---

## Steps to Run

### Option 1  - Jupyter Notebook
```
    jupyter notebook
```
- Open notebooks/midterm_project.ipynb
- Select a dataset when prompted
- Enter minimum support and confidence values
- View frequent itemsets, rules, and execution time comparison

### Option 2 - Python scripts

Run individual algorithms:

    ```
    python src/brute_force.py
    python src/apriori.py
    python src/fpgrowth.py
    ```
---

## Example Output

Frequent Itemsets:
``` 
['Milk', 'Bread'] : Support = 0.45
['Pen', 'Ink'] : Support = 0.40
```

Association Rules:
```
[Ink] -> [Pen] (support=0.40, confidence=1.0)
[Pen] -> [Ink] (support=0.40, confidence=0.67)
```

--- 

## Execution Time Comparison:

Algorithm	Time (seconds)
Brute Force	0.2919
Apriori	0.0272
FP-Growth	0.0119

--- 

## Takeaway

- Brute Force becomes infeasible for larger datasets.
- Apriori is efficient but slows down as transactions grow.
- FP-Growth is the most scalable and memory-efficient.
