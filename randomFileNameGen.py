import uuid

def generate_random_filename(extension):
    # Generate a random UUID (Universally Unique Identifier)
    unique_id = str(uuid.uuid4())
    
    # Combine the UUID with the desired file extension
    filename = f"{unique_id}.{extension}"
    return filename