# app/models.py
from pydantic import BaseModel

class ReceiptItem(BaseModel):
    shortDescription: str
    price: str

class Receipt(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[ReceiptItem]
    total: str
    