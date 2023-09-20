# 🎉 Knoetic BE Engineer (Data focused) test

Welcome and congratulations to this round of our BE Engineer test. Both **Python and SQL** expertise will be tested with an emphasis on the SQL.

---

### Grading

You will be graded based on the following:

- Code quality
- Strong understanding and application of Software Engineering principles
- Collaboration & communication skills

Our ultimate goal is to access how you work day to day, so apply the same seriousness and processes that you would in a real work environment.

---

## Set up instructions

Installing Flask. Make sure you have [pyenv](https://github.com/pyenv/pyenv#installation) installed. Use `Python 3.10.6`:

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

## The test (useful info)

- Google is allowed
- Hot reloading is set up
- Even though we are using [Flask](https://flask.palletsprojects.com/en/2.3.x/), knowledge of the framework is unimportant
- Feel free to use any SQL editor of your choice. You simply need to connect to our `instance/flaskr.sqlite` DB after intialising the database
- We have `#TODO` comments marked in `flaskr/solution.py` that we will be tackling one by one
