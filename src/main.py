# Import BaseModel from pydantic to define data models
from pydantic import BaseModel
from fastapi import FastAPI

# --- The Query Model ---
# This class defines the structure of a request we expect.
# It inherits from BaseModel, which gives it data validation powers.
class Query(BaseModel):
    """
    Represents a user's query sent to Cognitect.
    """
    # We expect a single field, 'text', which must be a string.
    text: str

# Create an instance of the FastAPI application.
app = FastAPI()

# Define a "route" using a function decorator.
@app.get("/")
def read_root():
    """
    This is the primary endpoint. It signifies that the core
    service is online and responsive.
    """
    return {"message": "Cognitect seed online. Awaiting instructions."}

# --- The New Endpoint ---
# This is where the magic happens. We define a POST endpoint.
# POST requests are used to send data to the server.
@app.post("/ask/")
def process_query(query: Query):
    """
    Receives a user's query, processes it, and returns a
    confirmation. This is the beginning of the dialogue.
    """
    # For now, our logic is simple.
    # We echo back the received text to confirm we heard it.
    # In the future, this is where the real intelligence will live.
    return {
        "response": f"Query received. You asked: '{query.text}'. Processing...",
        "received_data": query
    }