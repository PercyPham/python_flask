# python_flask

Need Python 3.10

Install `pipenv` (python package manager):

```
pip install --user pipenv
```

Install packages:

```
pipenv install
```

To activate this project's virtualenv (so we can run the app):

```
pipenv shell
```

Run app (windows):

```
python app.py
```

## Apis

Create User:
- url: `http://127.0.0.1:5000/users`
- method: `POST`
- body: `{ "name": "Any Name" }`

Get all users:
- url: `http://127.0.0.1:5000/users`
- method: GET
