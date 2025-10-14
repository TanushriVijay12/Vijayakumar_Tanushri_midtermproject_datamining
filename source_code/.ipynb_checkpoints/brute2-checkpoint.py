import os

# -----------------------------
# Load transactions
# -----------------------------
def load_transactions(filename):    
    transactions = []
    with open(filename, "r") as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split(",")
            items = [p.strip() for p in parts[3:]]
            transactions.append(items)
    return transactions

# -----------------------------
# Generate candidates of size k
# -----------------------------
def generate_candidates(items, k):
    candidates = []
    items = list(items)
    n = len(items)

    def helper(start, comb):
        if len(comb) == k:
            candidates.append(comb[:])
            return
        for i in range(start, n):
            comb.append(items[i])
            helper(i + 1, comb)
            comb.pop()

    helper(0, [])
    return candidates

# -----------------------------
# Compute support
# -----------------------------
def support_transactions(transactions, itemset):
    count = 0
    for t in transactions:
        if all(i in t for i in itemset):
            count += 1
    return count / len(transactions), count   # return fraction + raw count

# -----------------------------
# Find frequent itemsets
# -----------------------------
def frequent_itemsets(transactions, min_sup):
    unique_items = set(i for t in transactions for i in t)
    freq_is = {}
    k = 1

    while True:
        candidates = generate_candidates(unique_items, k)
        if not candidates:
            break

        print(f"\nTable C{k}: (Candidates)")
        valid = []
        for c in candidates:
            sup, count = support_transactions(transactions, c)
            print(f"{c}: count={count}, support={sup*100:.2f}%")
            if sup >= min_sup:
                valid.append((c, sup, count))

        if not valid:
            break

        print(f"\nTable L{k}: (Frequent itemsets)")
        for item, sup, count in valid:
            print(f"{item}: count={count}, support={sup*100:.2f}%")

        freq_is[k] = valid
        k += 1

    return freq_is

# -----------------------------
# Generate association rules
# -----------------------------
def generate_subsets(itemset):
    subsets = []
    def helper(start, current):
        if 0 < len(current) < len(itemset):
            subsets.append(current[:])
        for i in range(start, len(itemset)):
            current.append(itemset[i])
            helper(i + 1, current)
            current.pop()
    helper(0, [])
    return subsets

def generate_rules(freq_is, min_conf):
    rules = []
    for k in freq_is:
        for itemset, sup, count in freq_is[k]:
            if len(itemset) < 2:
                continue

            subsets = generate_subsets(itemset)
            for left in subsets:
                right = [x for x in itemset if x not in left]

                sup_left = None
                for size, sets in freq_is.items():
                    if size == len(left):
                        for c, s, cnt in sets:
                            if set(c) == set(left):
                                sup_left = s
                                break

                if sup_left and sup_left > 0:
                    conf = sup / sup_left
                    if conf >= min_conf:
                        rules.append((left, right, sup, conf))

    return rules

# -----------------------------
# Main
# -----------------------------
def main():
    datasets = {
        1: "amazon_transactions.csv",
        2: "bestbuy_transactions.csv",
        3: "walmart_transactions.csv",
        4: "nike_transactions.csv",
        5: "wholefoods_transactions.csv",
        6: "w3.csv"
    }

    print("AVAILABLE DATASETS:")
    for i, ds in datasets.items():
        print(f"{i}. {ds}")

    data_select = int(input("Choose which dataset to use: "))
    if data_select not in datasets:
        print("Invalid selection")
        return

    filename = os.path.join("..", "dataset", datasets[data_select])
    transactions = load_transactions(filename)

    min_sup = float(input("Enter the minimum support threshold (0-1): "))
    min_conf = float(input("Enter the minimum confidence threshold (0-1): "))

    freq_is = frequent_itemsets(transactions, min_sup)

    if not freq_is:
        print("\nNo frequent itemsets found.")
        return

    rules = generate_rules(freq_is, min_conf)
    if not rules:
        print("\nNo rules generated.")
        return

    print("\nFinal Association Rules:")
    for i, (left, right, sup, conf) in enumerate(rules, 1):
        print(f"Rule {i}: {left} -> {right}, "
              f"Support={sup*100:.2f}%, Confidence={conf*100:.2f}%")

if __name__ == "__main__":
    main()
