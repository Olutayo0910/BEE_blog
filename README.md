# BEE_blog

BEE_blog is a simple blog application built with Flask. It allows users to register, log in, and create blog posts. The application also features a home page that displays existing blog posts and an about page.

## Features

- User registration and login
- Creating and viewing blog posts
- Flash messages for successful and unsuccessful actions

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/BEE_blog.git
    cd BEE_blog
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Set the Flask environment variable:
    - On Windows:
        ```bash
        set FLASK_APP=run.py
        set FLASK_ENV=development
        ```
    - On macOS/Linux:
        ```bash
        export FLASK_APP=run.py
        export FLASK_ENV=development
        ```

6. Initialize the database:
    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

7. Run the application:
    ```bash
    flask run
    ```

## Usage

1. Visit the home page at `http://127.0.0.1:5000/home` to see existing blog posts.
2. Go to `http://127.0.0.1:5000/register` to create a new account.
3. Log in at `http://127.0.0.1:5000/login` using your registered credentials.
4. Create and view your blog posts.

## Project Structure

- `app.py`: The main application file containing routes and view functions.
- `models.py`: Contains database models for users and posts.
- `forms.py`: Contains WTForms classes for registration and login forms.
- `templates/`: Contains HTML templates for rendering the views.
- `static/`: Contains static files such as CSS and JavaScript.

## Routes

- `/home`: Home page displaying blog posts.
- `/about`: About page.
- `/register`: User registration page.
- `/login`: User login page.

## Example Data

Example blog posts are defined in the `app.py` file:

```python
posts = [
    {
        'username': 'Ola23',
        'title': 'My first blog',
        'date_created': '12 April',
        'content': 'This is my first blog'
    },
    {
        'username': 'Kez23',
        'title': 'My second blog',
        'date_created': '12 March',
        'content': 'This is my second blog'
    },
    {
        'username': 'Remi04 ',
        'title': 'My third blog',
        'date': '16 August',
        'content': 'This is my third blog'
    }
]
```

## Contributing
If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
