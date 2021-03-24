# CMS  API

# How it works

CMS API have 2 main objects:
- Content: Which is represented by a title and a body and an owner
- User: Which is represented by an email and a password which can be either a content auther and an administrator

## User side

An user can do the following things
- Login
- Perform CRUD operation on Content  created by him only

## Administrator side

An administrator can do the following things:
- Login
- Perform CRUD operation on Content


# Install the API

## Install manually

To install it, just clone the repository and run the following command:

`pip install -r cms/requirements.txt`

Or you can create a virtualenv like this:

```sh
virtualenv -p python3.6 venv
source venv/bin/activate
cd <CMS REPOSITARY>
pip install -r <CMS_REPOSITARY>/requirements.txt

#Make sure everything worked:
cd CMS_REPOSITORY>
python3 manage.py test
python3 manage.py migrate
python3 manage.py runserver
```

Just replace the `CMS_REPOSITORY` by the actual repository

**Make sure you have python3 installed**
# Run the server

To run the server simply use: `python3 manage.py runserver`

# Routes

In all paths containing a `PK`, replace the `PK` by the primary key

| Path                  | Description                                                             | Methods                   |
| --------------------- | ----------------------------------------------------------------------- | --------------------------|
| /api/token            | Used by the user to get authenticaton token                             | POST                      |
| /api/token            | Used by the user to logout                                              | DELETE                      |
| /api/user/            | Used by a new user to register and be able to log in                    | POST                      |
| /api/content          | List all content and allows you to create some                          | GET / POST                |
| /api/v1/content/PK    | Allows a basic CRUD on a specific content                               | GET / PUT / PATCH/ DELETE |

#TO seed admin

python3 manage.py loaddata seed/Admin.json
