# external_api.py
# Pretend this talks to a real HTTP API (slow / not implemented yet)

def get_user(user_id: int) -> dict:
    # In real life, this would call some external REST API.
    # We DO NOT want to run this in tests.
    raise NotImplementedError("Real API not implemented.")
