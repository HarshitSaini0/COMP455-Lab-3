import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Ensure all columns and full tables are printed in terminal output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)

# =====================================================================
# Task 1: Load and Prepare the Log Data
# =====================================================================
print("=" * 80)
print("TASK 1: LOAD AND PREPARE LOG DATA")
print("=" * 80)

# Load file handling arbitrary whitespace/tabs
df = pd.read_csv('comp455_logs.csv', sep=r'\s+', engine='python')

print("\n--- Part 1A: Original Log Data (First 5 Rows) ---")
print(df.head(5))

# Group unique event types by session_id
transactions = df.groupby('session_id')['event_type'].apply(lambda s: sorted(list(set(s)))).tolist()

# One-hot encode into Boolean transaction matrix
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

print(f"\nTotal sessions processed: {len(transactions)}")
print("\n--- Part 1B: Transformed Transaction Matrix (First 5 Sessions) ---")
print(df_transformed.head(5))

# =====================================================================
# Task 2: Find Frequent Itemsets (min_support = 0.15)
# =====================================================================
print("\n" + "=" * 80)
print("TASK 2: FREQUENT ITEMSETS (min_support = 0.15)")
print("=" * 80)

frequent_itemsets_15 = apriori(df_transformed, min_support=0.15, use_colnames=True)
frequent_itemsets_15 = frequent_itemsets_15.sort_values(by='support', ascending=False).reset_index(drop=True)

# Add itemset length column for readability
frequent_itemsets_15['length'] = frequent_itemsets_15['itemsets'].apply(lambda x: len(x))

print(f"\nTotal frequent itemsets found (support >= 0.15): {len(frequent_itemsets_15)}\n")
print(frequent_itemsets_15)

# =====================================================================
# Task 3: Association Rules (min_confidence = 0.60)
# =====================================================================
print("\n" + "=" * 80)
print("TASK 3: ASSOCIATION RULES (min_confidence = 0.60)")
print("=" * 80)

rules_60 = association_rules(frequent_itemsets_15, metric="confidence", min_threshold=0.60)
cols_display = ['antecedents', 'consequents', 'support', 'confidence', 'lift']

# Convert frozensets to lists/strings for clean printing
rules_display = rules_60[cols_display].copy()
rules_display['antecedents'] = rules_display['antecedents'].apply(lambda x: set(x))
rules_display['consequents'] = rules_display['consequents'].apply(lambda x: set(x))
rules_display = rules_display.sort_values(by='confidence', ascending=False).reset_index(drop=True)

print(f"\nTotal rules generated: {len(rules_display)}\n")
print(rules_display)

# =====================================================================
# Task 4: Compare Two Support Thresholds (0.15 vs 0.10)
# =====================================================================
print("\n" + "=" * 80)
print("TASK 4: COMPARE SUPPORT THRESHOLDS (0.15 vs 0.10)")
print("=" * 80)

frequent_itemsets_10 = apriori(df_transformed, min_support=0.10, use_colnames=True)
frequent_itemsets_10['length'] = frequent_itemsets_10['itemsets'].apply(lambda x: len(x))

print(f"Number of frequent itemsets at min_support = 0.15: {len(frequent_itemsets_15)}")
print(f"Number of frequent itemsets at min_support = 0.10: {len(frequent_itemsets_10)}")
print(f"Additional itemsets unlocked: {len(frequent_itemsets_10) - len(frequent_itemsets_15)}")

print("\n--- Distribution of Itemset Sizes (0.15 vs 0.10) ---")
print("Threshold 0.15 sizes:\n", frequent_itemsets_15['length'].value_counts().sort_index())
print("Threshold 0.10 sizes:\n", frequent_itemsets_10['length'].value_counts().sort_index())

# =====================================================================
# Task 5: Filter for Stronger Rules (confidence >= 0.70 & lift > 1.0)
# =====================================================================
print("\n" + "=" * 80)
print("TASK 5: STRONGER RULES (Confidence >= 0.70 & Lift > 1.0)")
print("=" * 80)

strong_rules = rules_display[(rules_display['confidence'] >= 0.70) & (rules_display['lift'] > 1.0)]
strong_rules = strong_rules.sort_values(by=['confidence', 'lift'], ascending=[False, False]).reset_index(drop=True)

print(f"\nTotal strong rules found: {len(strong_rules)}\n")
print(strong_rules)