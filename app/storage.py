# app/storage.py
# storage.py

import json
import uuid

# In-memory storage for receipts
receipts = {}

def add_receipt(receipt_data):
    # Generate a unique UUID for the receipt
    receipt_id = str(uuid.uuid4())
    # Store the receipt data with the UUID as the key
    receipts[receipt_id] = receipt_data
    return receipt_id

def get_receipt(receipt_id):
    # Retrieve the receipt data by UUID
    return receipts.get(receipt_id)