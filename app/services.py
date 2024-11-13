# app/services.py
from app.models import Receipt
from math import ceil
from .storage import receipts

def get_all_receipts():
    # Return all receipts as a list of values from the dictionary
    return list(receipts.values())

def get_receipt_by_id(receipt_id: str):
    # Directly retrieve the receipt by its UUID (receipt_id) from the dictionary
    return receipts.get(receipt_id)

def calculate_points(receipt: Receipt) -> int:
    points = 0

    # 1. Add points for alphanumeric characters in the retailer name
    points += sum(c.isalnum() for c in receipt.retailer)
    
    # 2. Add points if the total is a whole number
    if float(receipt.total).is_integer():
        points += 50

    # 3. Add points if the total is a multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
        points += 25

    # 4. Add 5 points for every pair of items
    points += (len(receipt.items) // 2) * 5

    # 5. Add points for items with descriptions that are multiples of 3 characters in length
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += ceil(float(item.price) * 0.2)

    # 6. Add 6 points if the purchase date day is an odd number
    if int(receipt.purchaseDate.split("-")[-1]) % 2 == 1:
        points += 6

    # 7. Add 10 points if the purchase time is between 2:00 PM and 4:00 PM
    hour, minute = map(int, receipt.purchaseTime.split(":"))
    if 14 <= hour < 16:
        points += 10

    return points