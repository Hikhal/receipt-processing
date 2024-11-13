# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import Receipt
from app.services import get_all_receipts, get_receipt_by_id, calculate_points
from app.storage import receipts
import uuid

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/receipts")
def read_receipts():
    return get_all_receipts()

@app.get("/receipts/{receipt_id}")
def read_receipt(receipt_id: str):
    receipt = get_receipt_by_id(receipt_id)
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return receipt

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    # Calculate points for the receipt
    points = calculate_points(receipt)
    
    # Generate a new UUID for the receipt
    receipt_id = str(uuid.uuid4())
    
    # Add the calculated points to the receipt data
    receipt_with_points = receipt.dict()
    receipt_with_points["points"] = points
    
    # Store the receipt with the UUID as the key
    receipts[receipt_id] = receipt_with_points
    
    return {"id": receipt_id}

@app.get("/receipts/{id}/points")
def get_points(id: str):
    # Retrieve the receipt data by ID
    receipt = receipts.get(id)
    
    if receipt is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    
    # Return the points stored with the receipt
    return {"points": receipt["points"]}