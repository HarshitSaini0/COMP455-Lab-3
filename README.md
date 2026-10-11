
# COMP 455 - Lab 3: Frequent Itemsets & Association Rules

This project analyzes security audit logs (`comp455_logs.csv`) containing 195 security events across 60 sessions. Using the Apriori algorithm and Association Rule Mining, log lines are grouped by session to identify recurring co-occurrence patterns and predictive security correlations (e.g., VPN connections leading to administrative scripts, or PowerShell activity preceding malware alerts).

---

## Project Structure

```text
.
├── comp455_logs.csv    # Raw security log dataset (whitespace/tab-separated)
├── main.py             # Data preparation script (inspecting raw vs. encoded data)
├── lab3.py             # Full end-to-end lab implementation (Tasks 1 to 5)
├── text.txt            # Captured output from main.py
├── lab3.txt            # Captured output from lab3.py
└── README.md           # Documentation and execution instructions

```

---

## Prerequisites & Installation

Ensure you have Python 3 installed along with `pandas` and `mlxtend`.

Install the required dependencies:

```bash
pip install pandas mlxtend

```

---

## File Descriptions

### 1. `main.py` (Data Understanding & Encoding)

Focuses on loading, parsing, and transforming the space/tab-delimited log data into the structure required by data mining algorithms:

* Reads `comp455_logs.csv` using the regex delimiter `sep=r'\s+'`.
* Sets pandas display flags to prevent column and row truncation (`...`).
* Groups unique `event_type` records per `session_id`.
* Utilizes `TransactionEncoder` to convert transactions into:
* A 2D Boolean NumPy array (`te_ary`).
* A structured one-hot encoded `DataFrame` (`df_transformed`).



### 2. `lab3.py` (Complete Lab Pipeline)

Implements all 5 lab questions:

* **Task 1:** Loads the data and transforms sessions into transaction itemsets.
* **Task 2:** Identifies frequent itemsets with `min_support = 0.15` and sorts by frequency.
* **Task 3:** Extracts association rules with `min_confidence = 0.60`.
* **Task 4:** Re-runs frequent itemset mining with `min_support = 0.10` and compares output distribution.
* **Task 5:** Filters for strong, non-random rules (`confidence >= 0.70` and `lift > 1.0`).

---

## How to Run & Redirect Output

To run the scripts and inspect the complete, non-truncated tables directly in text files, run:

### Inspecting Preparation Output (`main.py`):

```bash
cat | python main.py > text.txt

```

*(Press `Ctrl + D` if the terminal waits for standard input, or run `python main.py > text.txt` directly).*

### Running the Full Lab Suite (`lab3.py`):

```bash
cat | python lab3.py > lab3.txt

```

*(Press `Ctrl + D` if the terminal waits for standard input, or run `python lab3.py > lab3.txt` directly).*

---

## Viewing the Generated Results

View the formatted output files directly in your terminal:

```bash
# View data transformation breakdown
cat text.txt

# View full lab analysis (Tasks 1-5)
cat lab3.txt

# Or page through long tables
less lab3.txt

```

---

## Summary of Lab Deliverables

| Task | Objective | Key Output Metric |
| --- | --- | --- |
| **Task 1** | Session Aggregation | 60 transaction sessions, one-hot Boolean matrix |
| **Task 2** | Frequent Itemsets | Support $\ge 0.15$ (occurs in $\ge 9$ sessions) |
| **Task 3** | Association Rules | Confidence $\ge 0.60$ |
| **Task 4** | Threshold Sensitivity | Compares support $0.15$ vs $0.10$ ($6$ sessions) |
| **Task 5** | Rule Filtering | Confidence $\ge 0.70$ and Lift $> 1.0$ |
