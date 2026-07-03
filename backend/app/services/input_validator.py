MAX_CODE_LENGTH = 15000


def validate_input(code: str):

    if not code.strip():
        return {
            "valid": False,
            "message": "Please enter some Python code."
        }

    if len(code) > MAX_CODE_LENGTH:
        return {
            "valid": False,
            "message": "Code is too large to review."
        }

    return {
        "valid": True,
        "message": "Validation successful."
    }


def validate_project(files):

    if not files:
        return {
            "valid": False,
            "message": "No Python files found."
        }

    for file in files:

        validation = validate_input(file.content)

        if not validation["valid"]:
            return {
                "valid": False,
                "message": f"{file.path}: {validation['message']}"
            }

    return {
        "valid": True,
        "message": "Validation successful."
    }