import sqlite3
from datetime import datetime
import requests  

DISCORD_WEBHOOK_URL = "https://discordapp.com/api/webhooks/1517436304437149886/68oVsL40IUfqZ-UGhQ-fsMRLnwE-fugQ96JVFaAQhUviCzndSwhuz0t8GsL7cnFj0Qn2"

def generate_and_send_report():
    # 1. Connect to our existing database and run calculations
    conn = sqlite3.connect('company_sales.db')
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(price * quantity) FROM sales")
    total_revenue = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(quantity) FROM sales")
    total_units = cursor.fetchone()[0] or 0

    cursor.execute('''
        SELECT category, SUM(price * quantity) as category_revenue 
        FROM sales 
        GROUP BY category 
        ORDER BY category_revenue DESC 
        LIMIT 1
    ''')
    top_category_row = cursor.fetchone()
    top_category = top_category_row[0] if top_category_row else "N/A"
    top_category_revenue = top_category_row[1] if top_category_row else 0
    conn.close()

    current_date = datetime.now().strftime('%Y-%m-%d')

    report_message = f"""
📊 **WEEKLY BUSINESS PERFORMANCE REPORT** ({current_date})
```
========================================
Total Revenue:         ${total_revenue:,.2f}
Total Units Sold:      {total_units} units
----------------------------------------
Top Performing Category by Revenue:
👉 {top_category} (${top_category_revenue:,.2f})
========================================

🤖 Generated automatically by the Analytics Pipeline Engine.
"""

# 3. Package the data into the structure Discord expects (JSON)
    payload = {
        "content": report_message
    }

    # 4. Fire the data across the internet to Discord!
    print("Sending report to Discord...")
    response = requests.post(DISCORD_WEBHOOK_URL, json=payload)

    # 5. Check if it worked 
    if response.status_code == 204 or response.status_code == 200:
        print("Success! Report posted to Discord channel.")
    else:
        print(f"Failed to send report. Error code: {response.status_code}")

# ONLY these two lines should be all the way to the left at the very end:
if __name__ == "__main__":
    generate_and_send_report()



