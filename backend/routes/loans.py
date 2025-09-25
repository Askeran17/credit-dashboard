from fastapi import APIRouter, UploadFile
from database import db
from bson import ObjectId
from datetime import datetime  
from utils.csv_parser import parse_csv

router = APIRouter()

@router.post("/loans/import/{institution_id}")
async def import_loans(institution_id: str, file: UploadFile):
    contents = await file.read()
    with open("temp.csv", "wb") as f:
        f.write(contents)

    loans = parse_csv("temp.csv", institution_id)
    db.loans.insert_many(loans)
    return {"imported": len(loans)}

@router.get("/dashboard/{institution_id}")
def get_dashboard(institution_id: str):
    today = datetime.utcnow().date()

    # Обновляем статус займов, если срок истёк
    db.loans.update_many(
        {
            "institution_id": institution_id,
            "loan_last_date": {"$lt": today.isoformat()},
            "status": "ACTIVE"
        },
        {"$set": {"status": "EXPIRED"}}
    )

    # Получаем данные института
    inst = db.institutions.find_one({"_id": ObjectId(institution_id)})
    institution_name = inst.get("name") if inst else None

    # Получаем все займы
    loans = list(db.loans.find({"institution_id": institution_id}))
    for l in loans:
        if "_id" in l:
            l["_id"] = str(l["_id"])
        # добавляем имя института для удобства на фронте
        if institution_name and "name" not in l:
            l["name"] = institution_name

    total = sum(loan["principal_open_eur"] for loan in loans)
    invested = sum(loan["principal_open_eur"] for loan in loans if loan["status"] == "ACTIVE")
    percent = round((invested / total) * 100, 2) if total else 0

    return {
        "institution_id": institution_id,
        "institution_name": institution_name,
        "total_loan_eur": total,
        "invested_eur": invested,
        "invested_percent": percent,
        "loans": loans
    }


@router.get("/loans/{institution_id}")
def list_loans(institution_id: str):
    loans = list(db.loans.find({"institution_id": institution_id}))
    for l in loans:
        if "_id" in l:
            l["_id"] = str(l["_id"])
    return loans
