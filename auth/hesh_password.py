import hashlib

def hesh_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
