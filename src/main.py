# Import the FastAPI class from the library we just installed.
from fastapi import FastAPI

# Create an instance of the FastAPI application.
# This 'app' object is the central point of our entire API.
# It is the "heart" of the Cognitect seed.
app = FastAPI()

# Define a "route" using a function decorator.
# This tells FastAPI that any GET request to the root URL ("/")
# should be handled by the function below.
@app.get("/")
def read_root():
    """
    This is the primary endpoint. It signifies that the core
    service is online and responsive.
    """
    # Return a Python dictionary. FastAPI will automatically
    # convert this into a JSON response for the browser.
    return {"message": "Cognitect seed online. Awaiting instructions."}