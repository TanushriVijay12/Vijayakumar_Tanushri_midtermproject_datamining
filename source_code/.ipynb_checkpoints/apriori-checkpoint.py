# APRIORI
import os
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

#Load Data
def load_transactions(filename):
    transactions = []
    with open(filename, "r") as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split(",")
            items = [p.strip() for p in parts[3:]]
            transactions.append(items)
    return transactions

# Convert to one-hot encoded DataFrame
def transactions_to_df(transactions):
    all_items = sorted(set(i for t in transactions for i in t))
    df = pd.DataFrame(False, index=range(len(transactions)), columns=all_items)
    for i, t in enumerate(transactions):
        for item in t:
            df.loc[i, item] = True
    return df

def main():
    datasets = {
        1: "amazon_transactions.csv",
        2: "bestbuy_transactions.csv",
        3: "walmart_transactions.csv",
        4: "nike_transactions.csv",
        5: "wholefoods_transactions.csv"
    }

    print("AVAILABLE DATASETS:")
    for i, ds in datasets.items():
        print(f"{i}. {ds}")

    data_select = int(input("Choose which dataset to use: "))
    if data_select not in datasets:
        print("Invalid choice")
        return

    filename = os.path.join("..", "dataset", datasets[data_select])
    transactions = load_transactions(filename)

    min_sup = float(input("Enter minimum support (0-1): "))
    min_conf = float(input("Enter minimum confidence (0-1): "))

    df = transactions_to_df(transactions)

    # Run Apriori
    freq_itemsets = apriori(df, min_support=min_sup, use_colnames=True)
    if freq_itemsets.empty:
        print("No frequent itemsets found.")
        return

    print("\nFrequent Itemsets:")
    for _, row in freq_itemsets.iterrows():
        items = list(row['itemsets'])
        print(f"{items}: {row['support']:.2f}")

    # Generate Rules
    rules = association_rules(freq_itemsets, metric="confidence", min_threshold=min_conf)
    if rules.empty:
        print("No rules generated.")
        return

    print("\nAssociation Rules:")
    for _, row in rules.iterrows():
        left = list(row['antecedents'])
        right = list(row['consequents'])
        print(f"{left} -> {right} (support: {row['support']:.2f}, confidence: {row['confidence']:.2f})")

if __name__ == "__main__":
    main()
