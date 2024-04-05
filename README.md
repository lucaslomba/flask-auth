# 🔐 Flask auth
Example of a login authenticator using flask and python

## 🚀 Techs
Python, Flask, SQLAlchemy, SQLite


## 🛠️ Clone

To clone and run this application, you'll need Python installed on your computer.

📥 Clone the repository:

```bash
  git clone https://github.com/lucaslomba/flask-auth.git
```

📂 Navigate to the project directory:

```bash
  cd flask-auth
```

## 🛠️ Install dependencies

📥 Install using requirements.txt:

```bash
    pip3 install -r requirements.txt --upgrade
```

### Start project 

```bash
$ python3 app.py

```

## API Reference

### Login

```http
  POST api_url/login
```

Request body

```JSON
{
    "username": "string",
    "password": "string"
}
```

### Logout

```http
  GET api_url/logout
```

### Create user

```http
  POST api_url/user
```

Request body

```JSON
{
    "username": "string",
    "password": "string"
}
```

### Get user by ID

```http
  GET /api/user/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. |

### Update user by ID

```http
  PUT /api/user/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. |


## Authors

- [@lucaslomba](https://github.com/lucaslomba)

