# Automated Retail Analytics & Discord Alert Engine

## 📋 Project Overview

In fast-paced corporate environments, leadership teams rely on weekly performance updates but rarely have the time to hunt through raw databases or Excel sheets.

This project solves this bottleneck by introducing a fully automated backend data pipeline. The system runs completely hands-free to query a local database, calculate key weekly performance metrics using optimized SQL, format the findings into a stylized report, and instantly broadcast the results to a team collaboration channel (Discord) via a REST API webhook.

---

## ⚙️ How It Works (System Architecture)

The pipeline operates seamlessly in four distinct phases:

1. **Data Layer:** A local SQLite database houses structured retail transaction logs (products, categories, pricing, and quantities).
2. **Processing Layer:** A Python engine connects to the database and utilizes optimized SQL aggregation functions (`SUM`, `GROUP BY`) to extract performance insights in milliseconds.
3. **Notification Layer:** The script structures the raw insights into a JSON payload and transmits it across the internet using the Python `requests` library to a secure Discord Webhook.
4. **Orchestration Layer:** Windows Task Scheduler acts as the operating-system-level workflow manager, waking up the script automatically every week to trigger the alert hands-free.

---

## 🛠️ Tech Stack & Skills Demonstrated

- **Language:** Python 3
- **Database Management:** SQLite (`sqlite3`)
- **API Integration:** REST APIs, Discord Webhooks, and JSON data payloads
- **Network Operations:** Python `requests` library
- **Automation & Orchestration:** Windows Task Scheduler
- **Best Practices Demonstrated:** Parameterized queries (SQL Injection defense), API exception handling, clean architectural decoupling, and Markdown formatting for clear data visualization.

---

## 🚀 Getting Started

### Prerequisites

- Windows OS
- Python 3.x installed

### Installation & Execution

1. Clone this repository to your local machine.
2. Install the necessary network dependency:

   ```bash
   pip install requests
   ```

3. Initialize the local environment and generate the mock transaction data:

   ```bash
   python setup_db.py
   ```

4. Open `generate_report.py` and paste your unique Discord Webhook URL into the global variable:

   ```python
   DISCORD_WEBHOOK_URL = "YOUR_SECRET_URL"
   ```

5. Trigger the pipeline manually to test the integration:

   ```bash
   python generate_report.py
   ```

---

## 🔮 Future Roadmap (Production Upgrades)

To scale this into a multi-environment corporate asset, future iterations will focus on:

- **Securing Credentials:** Migrating the hardcoded Webhook URL out of the source code and into a `.env` file using `python-dotenv` to maintain industry-standard security.
- **Database Scalability:** Moving the local SQLite storage engine to an external cloud database instance like PostgreSQL hosted on AWS RDS.
- **Multi-Channel Routing:** Extending the notification layer to simultaneously deliver custom HTML emails via Amazon SES or SendGrid.
