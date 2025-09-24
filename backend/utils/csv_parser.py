import pandas as pd
from datetime import datetime

def parse_csv(file_path, institution_id):
    df = pd.read_csv(file_path)
    today = datetime.today().date()
    loans = []

    for _, row in df.iterrows():
        try:
            last_date = datetime.strptime(str(row['loan_last_date']), "%Y-%m-%d").date()
        except ValueError:
            last_date = today  # или continue

        status = "EXPIRED" if last_date < today else row.get('status', 'ACTIVE')

        loan = {
            **row.to_dict(),
            "status": status,
            "loan_url": f"https://loans.example.com/{row['loan_id']}",
            "institution_id": institution_id
        }
        loans.append(loan)

    return loans

