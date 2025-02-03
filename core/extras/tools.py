from uuid import uuid4
import random
import string


def generate_uuid():
    """Generate a unique identifier."""
    return uuid4()

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def generate_random_string(length=5):
    letters = string.ascii_lowercase
    return f"{''.join(random.choice(letters) for i in range(length))}"


def generate_random_email(length=5):
    return f"{generate_random_string(length)}@yopmail.com"


def generate_random_digits(n=8):
    return "".join(map(str, random.sample(range(0, 10), n)))



def generate_unique_code(prefix="MAT", length=6):
    """
    Génère un code unique.

    Args:
        prefix (str): Le préfixe du code (ex : "PROD" ou "CAT").
        length (int): Longueur du code sans le préfixe.

    Returns:
        str: Un code unique.
    """
    characters = string.ascii_uppercase + string.digits
    random_code = ''.join(random.choices(characters, k=length))
    
    
    product_code = f"{prefix}-{random_code}"
    
    return product_code


    
