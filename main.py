from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Pydantic model for an item
class Item(BaseModel):
    """Data model representing an item entity."""
    id: int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


# In-memory storage for items

items_db = []

# Create an item
@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    """
    Create a new item entry in the fake database[list].

    Args:
        item (Item): The item details to be created.

    Raises:
        HTTPException: If an item with the same ID already exists.

    Returns:
        Item: The newly created item entry.
    """
    for existing_item in items_db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items_db.append(item)
    return item

# Read all items
@app.get("/items/", response_model=List[Item])
async def read_items():
    """
    Retrieve a list of all item entries.

    Returns:
        List[Item]: A list containing all item entries in the fake database[list].
    """
    return items_db

# Read a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int):
    """
    Retrieve a specific item by its unique ID.

    Args:
        item_id (int): The unique identifier of the item to retrieve.

    Raises:
        HTTPException: If no item is found with the specified ID.

    Returns:
        Item: The item entry that matches the given ID.
    """
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found.")

# Update an item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, updated_item: Item):
    """
    Update an existing item entry with new details.

    Args:
        item_id (int): The unique identifier of the item to update.
        updated_item (Item): The updated item details.

    Raises:
        HTTPException: If no item is found with the specified ID.

    Returns:
        Item: The updated item entry.
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found.")

# Delete an item
@app.delete("/items/{item_id}", status_code=204)
async def delete_item(item_id: int):
    """
    Delete an item entry from the database by its unique ID.

    Args:
        item_id (int): The unique identifier of the item to delete.

    Raises:
        HTTPException: If no item is found with the specified ID.

    Returns:
        None: This endpoint returns no content upon successful deletion.
    """
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return None
    raise HTTPException(status_code=404, detail="Item not found.")

