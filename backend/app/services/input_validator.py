def validate_input(code: str):

    if not code.strip():
        return {
            "valid": False,
            "message": "Please enter some Python code."
        }

    if len(code) > 15000:
        return {
            "valid": False,
            "message": "Code is too large to review."
        }

    return {
        "valid": True,
        "message": "Validation successful."
    }