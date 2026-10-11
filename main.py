import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

# 1. Load the original log data (handling space/tab separation)
df = pd.read_csv('comp455_logs.csv', sep=r'\s+', engine='python')
import pandas as pd

# Show every column without '...'
pd.set_option('display.max_columns', None)

# Show wide rows without wrapping onto multiple lines
pd.set_option('display.width', 1000)

# Optional: show every row without truncating if a table is long
pd.set_option('display.max_rows', None)

print("=== PART 1: ORIGINAL DATA (First 5 Rows) ===")
print(df[['session_id', 'event_type']].head())

# 2. Group event_type by session_id into lists (Transactions)
transactions = df.groupby('session_id')['event_type'].apply(lambda events: list(set(events))).tolist()

# 3. Transform into the one-hot encoded matrix needed for Apriori
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
print("\n=== PART 1.5: ONE-HOT ENCODED TRANSACTION DATA (First 5 Sessions) ===")
print(te_ary)
df_transformed = pd.DataFrame(te_ary, columns=te.columns_)

print("\n=== PART 2: TRANSFORMED TRANSACTION DATA (First 5 Sessions) ===")
print(df_transformed)