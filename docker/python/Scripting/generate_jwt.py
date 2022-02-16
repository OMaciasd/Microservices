import jwt
import datetime

SECRET_KEY = "supersecret"
payload = {
    "user": "example_user",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=3600)
}
encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(encoded_jwt)
