# Brute force to find for finding frequent itemsets and assocition rules

import os

# Load Data
def load_transactions(filename):    
    transactions = []
    with open(filename, "r") as f:
        next(f)
        for line in f:
            parts = line.strip().split(",")
            items = [p.strip() for p in parts[3:]]
            transactions.append(items)
    return transactions

# Generate candidate items
def generate_candidates(items, k):
    candidates = []
    n = len(items)
    items = list(items)

    def helper(start, comb):
        if len(comb) == k:
            candidates.append(comb[:])
            return
        for i in range(start, n):
            comb.append(items[i])
            helper(i+1, comb)
            comb.pop()

    helper(0, [])
    return candidates

def support_transactions(transactions, item):
    count = 0
    for t in transactions:
        if all(i in t for i in item):
            count += 1
    return count/len(transactions)

# Generate frequent itmsets from candidate items
def frequent_itemsets(transactions, min_sup):
    unique_items = set()
    for t in transactions:
       for i in t:
           unique_items.add(i)

    freq_is = {}
    k=1

    while True:
        candidates = generate_candidates(unique_items, k)
        valid = []
        for c in candidates:
            sup = support_transactions(transactions, c)
            if sup >= min_sup:
                valid.append((c, sup))
        if not valid:
            break
        freq_is[k] = valid
        k += 1

    return freq_is
    
# Association rule mining
def generate_rules(freq_is, min_conf):
    rules = []
    # Loop over all frequent itemsets
    for k in freq_is:
        for itemset, sup in freq_is[k]:
            if len(itemset) < 2:
                continue

            # generate all possible non-empty proper subsets
            subsets = generate_subsets(itemset)

            for left in subsets:
                right = [x for x in itemset if x not in left]

                # Find support of the antecedent (left side)
                sup_left = None
                for size, sets in freq_is.items():
                    if size == len(left):
                        for c, s in sets:
                            if set(c) == set(left):
                                sup_left = s
                                break

                # Calculate confidence - if antecedent support exists
                if sup_left and sup_left > 0:
                    conf = sup / sup_left
                    if conf >= min_conf:
                        rules.append((left, right, sup, conf))

    return rules
    
# Generate all subsets of a given itemset (except empty and full set)
def generate_subsets(itemset):
    subsets = []

    def helper(start, current):
        if 0 < len(current) < len(itemset):
            subsets.append(current[:])   # store a copy
        for i in range(start, len(itemset)):
            current.append(itemset[i])
            helper(i + 1, current)
            current.pop()

    helper(0, [])
    return subsets

def main():
    # User input
    # 1. Transaction database
    datasets = {1: "amazon_transactions.csv",2: "bestbuy_transactions.csv", 3: "walmar_transactions.csv",4: "nike_transactions.csv",5: "wholefoods_transactions.csv"}
    print("AVAILABLE DATASETS:")
    for i, ds in datasets.items():
        print(f"{i}. {ds}")

    print("\n")    
    # Data choice
    data_select  = int(input("Choose which dataset to use: "))
    if data_select not in datasets:
        print("Invalid selection")
        return

    # filename = "dataset/" + datasets[data_select]
    filename = os.path.join("..", "dataset", datasets[data_select])
    transactions = load_transactions(filename)
    print("\n")
    
    # 2. Minimum support threshold
    min_sup = float(input("Enter the minimum support threshold(0-1): "))
    # 3. Minimum confidence threshold
    min_conf = float(input("Enter the minimum confidence threshold(0-1): "))

    print("\n")
    freq_is = frequent_itemsets(transactions, min_sup)
    # Print frequent itemsets
    for k, items in freq_is.items():
        print("\n")
        print(f"Frequent itemsets of size {k}:")
        for item, sup in items:
            print(f"{item}: {sup:.2f}")

    rules = generate_rules(freq_is, min_conf)
    print("\n")
    # Print association rules
    print("Association rules:")
    for left, right, sup, conf in rules:
        print(f"{left} -> {right}: (support: {sup:.2f}, confidence: {conf:.2f})")
# Run program
if __name__ == "__main__":
    main()