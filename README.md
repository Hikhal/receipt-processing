Receipt Processing API

This project is a FastAPI-based RESTful API designed to process purchase receipts, calculate reward points based on predefined rules, and store receipt data in memory. Each submitted receipt is assigned a unique identifier (UUID), allowing users to query the points associated with a particular receipt.

Project Structure

Here’s a breakdown of the main files and their responsibilities:


- **`app/main.py`:**  
  This file contains the core setup for the FastAPI application and defines all endpoints.  
  It handles requests for processing receipts, retrieving all receipts, fetching details for individual receipts by UUID, and querying the points associated with specific receipts.

- **`app/models.py`:**  
  This file defines the data models using Pydantic.  
  These models enforce the structure of receipt data, ensuring that each receipt has valid and correctly formatted fields, such as retailer, purchaseDate, purchaseTime, etc.

- **`app/services.py`:**  
  This file encapsulates the business logic of the application.  
  It includes functions to calculate points based on receipt data, retrieve all receipts, find specific receipts by UUID, and perform other helper tasks.  
  The `calculate_points` function applies specific rules to determine reward points based on the receipt’s properties, such as the retailer name, total amount, purchase date, and item descriptions.

- **`app/storage.py`:**  
  This file acts as a simple in-memory storage for the receipts.  
  For this implementation, it’s a dictionary that temporarily holds receipt data while the application is running.  
  It can later be modified or replaced with a database solution if persistence is needed.

