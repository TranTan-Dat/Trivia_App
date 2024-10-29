# Backend - Trivia API
The backend for this Trivia app is a lightweight Flask application designed to power a web-based quiz game. 
It leverages SQLAlchemy to define and manage the database, which stores various trivia questions, categories. 
Player not only answer the question, but also create question and answer, select the difficult point and category type.
Through a set of well-defined API endpoints, the app provides access to quiz content, supports gameplay functionality.
This setup creates a seamless experience for users, enabling interactive gameplay and efficient data retrieval directly from the database.
## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

```bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. From the `backend` folder in terminal run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## To Do Tasks

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/test_flaskr.py`

One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle `GET` requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle `GET` requests for all available categories.
4. Create an endpoint to `DELETE` a question using a question `ID`.
5. Create an endpoint to `POST` a new question, which will require the question and answer text, category, and difficulty score.
6. Create a `POST` endpoint to get questions based on category.
7. Create a `POST` endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a `POST` endpoint to get questions to play the quiz. This endpoint should take a category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422, and 500.

## Documenting your Endpoints

You will need to provide detailed documentation of your API endpoints including the URL, request parameters, and the response body. Use the example below as a reference.

## Overview
This API provides endpoints for managing questions and categories for a trivia application. The API is built with Flask and uses SQLAlchemy for database interactions.
### Base URL
`http://127.0.0.1:5000`
### Documentation Example

`GET '/api/v1.0/categories'`

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, `categories`, that contains an object of `id: category_string` key: value pairs.

```json
{
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```

`GET '/api/v1.0/questions'`
- Fetches a paginated list of questions.
- Request Arguments:
    - `page` (integer): The page number to get data.
- Returns: An object with the keys questions, total_questions, categories, and current_category.

```json
{
  "success": true,
  "questions": [
    {
      "id": 1,
      "question": "What is the capital of France?",
      "answer": "Paris",
      "category": 1,
      "difficulty": 1
    },
    ...
    {
      "id": 4,
      "question": "What is the capital of Vietnam?",
      "answer": "HaNoi",
      "category": 1,
      "difficulty": 1
    }
  ],
  "total_questions": 100,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null
}
```

`DELETE '/api/v1.0/questions/<int:question_id>'`
- Delete question by its id input.
- Request Arguments: None, just need id from url
- Returns: An object with the key deleted indicating the ID of the deleted question.
```json 
    {"deleted":4,"success":true}
```
- `4` is the id from url

`POST '/api/v1.0/questions'`
- Creates a new question
- request body:
```json 
{"question": "What is the capital of Vietnam?", "answer": "HaNoi", "difficulty": 1, "category": "3"}
```
- Return an example object like:
```json
{"created":34,"success":true}
```

`POST '/api/v1.0/questions/search'`
- Searches for questions by text input.
- Request Body:
```json
{"searchTerm": "capita"}
```
- Return example object:
```json
{
    "current_category": null,
    "questions": [
        {
            "answer": "Paris",
            "category": 1,
            "difficulty": 1,
            "id": 28,
            "question": "What is the capital of France?"
        },
        {
            "answer": "HaNoi",
            "category": 3,
            "difficulty": 1,
            "id": 34,
            "question": "What is the capital of Vietnam?"
        }
    ],
    "success": true,
    "total_questions": 2
}
```

`GET '/api/v1.0/categories/<int:category_id>/questions'`
- Get all questions that belong to a specific category.
- Request Arguments: `id` - integer
- Return An object with the keys questions, total_questions, and current_category.
```json
{
    "current_category": "Science",
    "questions": [
        {
            "answer": "The Liver",
            "category": 1,
            "difficulty": 4,
            "id": 20,
            "question": "What is the heaviest organ in the human body?"
        },
        {
            "answer": "Alexander Fleming",
            "category": 1,
            "difficulty": 3,
            "id": 21,
            "question": "Who discovered penicillin?"
        },
        {
            "answer": "Blood",
            "category": 1,
            "difficulty": 4,
            "id": 22,
            "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true,
    "total_questions": 3
}
```

`POST '/api/v1.0/quizzes'`
- Retrieves a random question for the quiz, avoiding previously asked questions.
- Request Body:
```json
{"previous_questions":[9],"quiz_category":{"type":"History","id":"4"}}
```
- Return an object with the key question indicating the next question for the quiz and list of previous question Id user already answered.
```json 
{
    "question": {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
    },
    "success": true
}
```

## Testing
To deploy the tests, run

```bash
dropdb trivia
createdb trivia
psql trivia < trivia.psql
python3 test_flaskr.py

```
