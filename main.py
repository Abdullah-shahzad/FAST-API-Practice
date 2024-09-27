from typing import Union

from fastapi import FastAPI

app = FastAPI()

#Create a simple "Hello World" application and run it with Uvicorn
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


fake_items_db = [
    {"item_id": 1, "name": "Apple", "category": "Fruit"},
    {"item_id": 2, "name": "Carrot", "category": "Vegetable"},
    {"item_id": 3, "name": "Banana", "category": "Fruit"},
]


@app.get("/items/{item_id}")
async def read_item(item_id: int, category: Union[str, None] = None):
    """
    This route captures `item_id` as a path parameter and
    filters the items based on the `category` query parameter.
    """
    for item in fake_items_db:
        if item["item_id"] == item_id:
            if category and item["category"].lower() == category.lower():
                return {"item": item, "filtered_by_category": category}
            return {"item": item}

    return {"error": "Item not found"}


#Define routes using HTTP methods (GET, POST, PUT, DELETE)

@app.get("/items/")
async def get_items():
    """
    Handles GET requests to fetch all items.
    """
    return {"message": "Fetching all items"}

@app.post("/items/")
async def create_item():
    """
    Handles POST requests to create a new item.
    """
    return {"message": "Item created"}


@app.put("/items/{item_id}")
async def update_item(item_id: int):
    """
    Handles PUT requests to update an existing item.
    """
    return {"message": f"Item {item_id} updated"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    """
    Handles DELETE requests to delete an item.
    """
    return {"message": f"Item {item_id} deleted"}



