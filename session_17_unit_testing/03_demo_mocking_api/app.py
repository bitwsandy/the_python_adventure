# app.py

import external_api

def get_user_name(user_id: int) -> str:
    """
    Our app logic:
    - Calls external_api.get_user(user_id)
    - Returns the 'name' field from the response
    """
    user = external_api.get_user(user_id)
    return user["name"]

get_user_name(2)
