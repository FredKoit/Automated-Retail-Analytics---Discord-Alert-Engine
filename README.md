# Automated Weekly Sales Analytics Engine

## Project Overview

In many corporate environments, data analysts and managers spend hours every week manually exporting data from production systems, writing Excel formulas, and formatting performance summaries for stakeholders.

This project solves that operational bottleneck by introducing a lightweight, fully automated backend data pipeline. The system runs completely hands-free to query an internal database, calculate key business metrics, and generate standardized, timestamped CSV reports ready for business intelligence (BI) consumption.

---

## How It Works (System Architecture)

The pipeline operates in four distinct phases:

1. **Data Layer:** A local SQLite database houses structured retail transaction logs (products, categories, pricing, and quantities).
2. **Processing Layer:** A Python engine connects to the database and utilizes optimized SQL aggregation functions (`SUM`, `GROUP BY`) to extract performance insights in milliseconds.
3. **Output Layer:** The script processes the raw data and exports a structured, timestamped CSV report (`weekly_report_YYYY-MM-DD.csv`), ensuring historical data retention without overwriting previous logs.
4. **Orchestration Layer:** Windows Task Scheduler acts as the operating-system-level workflow manager, waking up the system automatically every week to trigger the pipeline without human intervention.

---

## Tech Stack & Skills Demonstrated

- **Language:** Python 3
- **Database Management:** SQLite / `sqlite3`
- **Data Formatting:** Native `csv` & `datetime` libraries
- **Automation & Orchestration:** Windows Task Scheduler
- **Best Practices Demonstrated:** Parameterized queries (SQL Injection prevention), automated environment setup, local file system management, and precise absolute path mapping.

---

## Getting Started

### Prerequisites

- Windows OS
- Python 3.x installed

### Installation & Execution

1. Clone this repository to your local machine.
2. Initialize the local database and populate it with mock transaction data:
   ```bash
   python setup_db.py
   ```
3. Run the analytical reporting engine manually to verify the output:

```bash
   python generate_report.py
```

Check your project folder for the newly generated weekly*report*[CURRENT_DATE].csv file.

Note: To automate this project permanently on your local machine, map generate_report.py to a weekly trigger inside the Windows Task Scheduler desktop application.
