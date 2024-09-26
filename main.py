from fastapi import FastAPI

app = FastAPI()

#Create a simple "Hello World" application and run it with Uvicorn
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}



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