import io
import csv
from datetime import date, timedelta


def _create_inst(client):
    r = client.post("/api/institutions", json={
        "name": "Bank",
        "country": "SE",
        "founding_year": 2019,
        "total_portfolio": 100,
        "credit_risk_score": 0.1,
        "product_type": "Business",
        "website_url": "https://bank.example",
        "contacts": ["a@b.com"]
    })
    return r.json()["id"]


def _csv_bytes(rows):
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
    return buf.getvalue().encode()


def test_import_and_dashboard(test_client):
    inst_id = _create_inst(test_client)

    today = date.today()
    future = (today + timedelta(days=5)).isoformat()
    past = (today - timedelta(days=5)).isoformat()

    rows = [
        {"loan_id": "1", "loan_no": "10001", "loan_type": "X", "loan_date": today.isoformat(), "loan_last_date": future, "principal_open": 0, "principal_open_eur": 10000, "status": "ACTIVE", "loan_url": ""},
        {"loan_id": "2", "loan_no": "10002", "loan_type": "X", "loan_date": today.isoformat(), "loan_last_date": past,   "principal_open": 0, "principal_open_eur": 5000,  "status": "ACTIVE", "loan_url": ""},
    ]
    data = _csv_bytes(rows)

    files = {"file": ("loans.csv", data, "text/csv")}
    r = test_client.post(f"/api/loans/import/{inst_id}", files=files)
    assert r.status_code == 200
    assert r.json()["imported"] == 2

    # dashboard should mark past loan as EXPIRED and compute totals
    r = test_client.get(f"/api/dashboard/{inst_id}")
    assert r.status_code == 200
    body = r.json()
    assert body["total_loan_eur"] == 15000
    # invested only ACTIVE (future) = 10000
    assert body["invested_eur"] == 10000
    assert body["invested_percent"] == 66.67
    statuses = sorted(l["status"] for l in body["loans"]) 
    assert statuses == ["ACTIVE", "EXPIRED"]
