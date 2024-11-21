Here’s a guide on how to handle each of the tasks you've mentioned in a Flask app:

---

### **1. Declaring API Routes in a Flask App**

You define API routes using Flask's `@app.route()` decorator. Here's an example:

```python
from flask import Flask

app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return "Welcome to the homepage!"

# Define a route with a variable
@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"

# Define a route with a specific HTTP method
@app.route('/submit', methods=['POST'])
def submit_form():
    return "Form submitted!"
```

---

### **2. How to Get and Set Cookies**

Flask provides `request` to access cookies and `make_response` to set them.

#### Getting Cookies:
```python
from flask import request

@app.route('/get-cookie')
def get_cookie():
    cookie_value = request.cookies.get('my_cookie')
    return f"The value of 'my_cookie' is: {cookie_value}"
```

#### Setting Cookies:
```python
from flask import make_response

@app.route('/set-cookie')
def set_cookie():
    response = make_response("Cookie is set!")
    response.set_cookie('my_cookie', 'cookie_value')
    return response
```

---

### **3. How to Retrieve Request Form Data**

You can retrieve data from a form submitted via `POST` using `request.form`.

#### Example:
```python
from flask import request

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Name: {name}, Email: {email}"
```

---

### **4. How to Return Various HTTP Status Codes**

Flask allows you to return a response along with an HTTP status code.

#### Examples:

- **Default 200 OK**:
  ```python
  @app.route('/success')
  def success():
      return "Success!"
  ```

- **Custom Status Code**:
  ```python
  @app.route('/not-found')
  def not_found():
      return "This page was not found.", 404
  ```

- **Using `make_response` for Complex Responses**:
  ```python
  from flask import make_response

  @app.route('/unauthorized')
  def unauthorized():
      response = make_response("You are not authorized", 401)
      response.headers["Custom-Header"] = "Custom-Value"
      return response
  ```

---

Let me know if you'd like more examples or explanations!