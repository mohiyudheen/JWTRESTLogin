## Steps To Run Project

Step 1: Create Virtual environment. virtualenv venv
        
Step 2: Activate virtual environment.  source venv/bin/activate

Step 3: then install modules. pip install -r requirements.txt

Step 4: Run project. python manage.py runserver

## Obtain Token

First step is to authenticate and obtain the token. The endpoint is /api/login/ and it only accepts POST requests.


http post http://127.0.0.1:8000/api/login/ username=user1 password=adminadmin@123

So basically your response body is the two tokens:

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNjQ5ODU4NCwianRpIjoiNWUxZWMxNmI3OTAxNGU5NGFiOTY4OTI3NTY1MjVjOTAiLCJ1c2VyX2lkIjoyLCJmaXJzdF9uYW1lIjoidXNlcjEifQ.KIHzG5bjSu-CdOuzHnYv2qvgZtLgWHgdNBPiuVlujIE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2NDEyNDg0LCJqdGkiOiI2ODlkY2YwMGU2MGE0ODMxOWI2ZjQ0NWRlZDc3YTVlZSIsInVzZXJfaWQiOjIsImZpcnN0X25hbWUiOiJ1c2VyMSJ9.ZvL8M6rSiqib96b8dUrgCG4w70A4sgYSzB2_ZzIAy3s"
}


## To Verify token here https://jwt.io/


{
  "token_type": "access",
  "exp": 1626412484,
  "jti": "689dcf00e60a48319b6f445ded77a5ee",
  "user_id": 2,
  "first_name": "user1"
}

