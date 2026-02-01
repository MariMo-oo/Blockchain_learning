# Blockchain Proof-of-Work Simulation

This repository contains a Python implementation of a toy blockchain with a Proof-of-Work mechanism and an optional difficulty experiment with graph plotting.

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Script
```bash
python generate_chain.py
```

### 4. Runtime Inputs
When the program starts, you will be prompted for the following inputs:

**Difficulty Parameter (k)**
- Enter a positive integer (e.g., `1`, `2`, `3`, `4`, `5`)
- This value specifies the number of leading hexadecimal zeros required in the block hash

**Difficulty Experiment Option**
- Enter `Y` to run the difficulty experiment and generate a graph
- Enter `N` to only generate the blockchain CSV file

### 3. Run the validate Script
```bash
python validate_chain.py
```
This script validates and reports if the chain is valid.
