# Stock Market Service

## Deploy Server locally
1. Create virtual enviroment ( Recommended )
2. Install project requirements
3. Create .env file
4. Apply migrations
5. Run Collectstatic
6. Run Server

---
### 1- Create virtual environment ( Recommended )
 Create virtual environment. I suggest to user venv
```
python3 -m venv .venv
source .venv/bin/activate
```

### 2- Install project requirements
`pip install -r requirements.txt`

### 3- Create .env file
Create .env file using the .env-example file
### 4- Apply migrations
`python manage.py migrate`

### 5- Run Collectstatic
`python manage.py collectstatic`

### 6- Run Server
`python manage.py runserver`

---
---
## API Docs
1. Create User
2. Get API key
3. Requests


## 1 - Create User
method=*POST*

endpoint= `/api/v1/SMSUsers/sign_up/`

payload=
```
{
    "username": "Username",
    "password": "randomPassword",
    "email": "userEmail",
    "name": "userFirstName",
    "last_name": "userLastName"
}
```

## 2 - Get API key
method=*POST*

endpoint= `/api/v1/SMSUsers/get-api-key/`

payload=
```
{
    "username": "Username",
    "password": "randomPassword",
}
```

response=
```
{
     "message": "User API KEY: CAejmnsr5UvZDuFIpwKLU0kizHz6EIPCH1l31B9lx3O5R4vVpDH_OGh7aS9ox5Jf_8swyQmXEs785tN7"
}
```
*Use that API for making requests*

## 3 - Requests
method=*GET*

endpoint= `/api/v1/stocks`

**Important:** include the API KEY in the headers.

payload=
```
{
    "symbol": "ANYSUPPORTEDSYMBOL"
}
```

response=
```
{
    "message": "{'open': '112.6400', 'high': '113.6800', 'lower': '108.3700', 'variation': -2126.52}"
}
```
# Stock-Market-Service-Eureka
