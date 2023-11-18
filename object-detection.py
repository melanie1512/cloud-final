import boto3
from PIL import Image

# reemplazar por credenciales de AWS
session = boto3.Session(
    region_name='us-east-1',
    aws_access_key_id='ASIAWIH4AK3Q46LVU4GE',
    aws_secret_access_key='+PhgmDO/uLBlAFToj9OfgXT0KHE1X/H8Xe4ukj8K',
    aws_session_token='FwoGZXIvYXdzEI7//////////wEaDBIepqUH12EaHLk6sSK/ASuI7DIu0QXAeB3BJzGwBEpmYs/nXxnRKjMqV6LlPdky+5C6Ga4cthXUc4WNv8iukQ/f4KXmUNh+FLZ2OuHOC01rQG/FScyM8PLG9k5QcYQy8svvLaOT8Rjm0hbmjzP7FC9g7b4zgrL5M32dty/tMrtkxSNXPsiipTzbYVgQ0fmrOqY1gVn3FPMiIys+8xRNNzsPBYULmReypAn+VbLA0jVDW6El0O0m42u0p72JdZV4QEXAjanMsGdxePMdsqJrKPfC5KoGMi27paCG5rKXdKafow4MocFrCvQOdAg5xdDIx7rQtmJWh3QpOuXhzoDIMa/0hm0='
)

client = session.client('rekognition')

photo = "test1.jpg"

with open(photo, 'rb') as image_file:
    source_bytes = image_file.read()

detect_objects = client.detect_labels(Image={'Bytes': source_bytes})
print(detect_objects)