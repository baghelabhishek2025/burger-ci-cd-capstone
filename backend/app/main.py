from fastapi import FastAPI

app = FastAPI(title="Burger CI/CD Capstone API")

menu = [
    {
        "id": 1,
        "name": "Veg Grilled Paneer Burger",
        "description": "Soft sesame bun with grilled paneer, green chutney, cucumber, onion and tomato.",
        "price": 4.0,
        "currency": "CAD",
    },
    {
        "id": 2,
        "name": "Combo: 2 Burgers + Potato Wings",
        "description": "Two veg grilled paneer burgers served with crispy potato wings.",
        "price": 10.0,
        "currency": "CAD",
    },
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/menu")
def get_menu():
    return {"items": menu}
