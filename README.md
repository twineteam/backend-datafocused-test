# Getting started

### Set up

Make sure you have pyenv installed. Use `Python 3.10.6`:

```
pyenv install 3.10.6
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
pyenv activate 3.10.6
pip install Flask
```

#### Initializing & seeding the Database

```
flask --app flaskr init-db
```

#### Initializing the Server

```
flask --app flaskr run --debug
```

#### **Debugging**

Feel free to use any SQL editor of your choice. You simply need to connect to our `instance/flaskr.sqlite` DB after intialising the database
