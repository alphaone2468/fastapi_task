def individual_serial(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "name": todo["name"],
        "age": todo["age"],
        "address": todo["address"]
    }

def list_serial (todos) -> list:
    return [individual_serial(todo) for todo in todos]