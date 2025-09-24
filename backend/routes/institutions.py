from fastapi import APIRouter
from models import CreditInstitution
from database import db
from bson import ObjectId 

router = APIRouter()

@router.post("/institutions")
def create_institution(institution: CreditInstitution):
    result = db.institutions.insert_one(institution.dict())
    return {"id": str(result.inserted_id)}

@router.get("/institutions")
def list_institutions():
    """Return all institutions with stringified _id for convenience in Swagger."""
    items = list(db.institutions.find())
    for it in items:
        it["_id"] = str(it["_id"])  # make JSON-serializable
    return items

@router.delete("/institutions/{id}")  
def delete_institution(id: str):
    db.institutions.delete_one({"_id": ObjectId(id)})
    db.loans.delete_many({"institution_id": id})
    return {"status": "deleted"}
