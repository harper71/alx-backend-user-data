Here’s an overview of each concept, including how to implement a log filter, encrypt passwords, check validity, and authenticate using environment variables.

---

1. **Examples of Personally Identifiable Information (PII)**

- **PII** includes any information that can uniquely identify an individual. Common examples:
  - **Name**
  - **Address**
  - **Phone Number**
  - **Email Address**
  - **Social Security Number (SSN)**
  - **Bank Account or Credit Card Numbers**
  - **Date of Birth**
  - **Driver’s License Number**
  - **Biometric Data (e.g., fingerprints, facial recognition)**

---

2. **Implementing a Log Filter to Obfuscate PII Fields**

   When handling logs that contain PII, obfuscating sensitive data helps protect user privacy. Here’s a basic way to implement a log filter in Python that masks specific fields:

   ```python
   import re

   def mask_pii(log_message):
       # Patterns for common PII
       email_pattern = r"[\w\.-]+@[\w\.-]+"
       phone_pattern = r"\b\d{3}[-.\s]??\d{2}[-.\s]??\d{4}\b"
       ssn_pattern = r"\b\d{3}-\d{2}-\d{4}\b"

       # Mask PII in the log message
       log_message = re.sub(email_pattern, "[EMAIL]", log_message)
       log_message = re.sub(phone_pattern, "[PHONE]", log_message)
       log_message = re.sub(ssn_pattern, "[SSN]", log_message)

       return log_message

   # Example usage
   log = "User email: user@example.com, phone: 555-123-4567, SSN: 123-45-6789"
   print(mask_pii(log))
   ```

   This function replaces any detected emails, phone numbers, or SSNs with placeholders.

---

3. **Encrypting a Password and Validating Input**

   Passwords should be stored using secure hashing algorithms rather than plain text. Here’s an example using Python’s `bcrypt` library.

   ```python
   import bcrypt

   # Encrypting a password
   def hash_password(password):
       # Generate salt and hash password
       salt = bcrypt.gensalt()
       hashed = bcrypt.hashpw(password.encode(), salt)
       return hashed

   # Checking password validity
   def check_password(stored_hash, password_input):
       return bcrypt.checkpw(password_input.encode(), stored_hash)

   # Example usage
   user_password = "SuperSecurePassword123"
   stored_hash = hash_password(user_password)

   # Verifying user input against stored hash
   password_input = "SuperSecurePassword123"
   if check_password(stored_hash, password_input):
       print("Password is valid.")
   else:
       print("Invalid password.")
   ```

- `hash_password()` generates a secure hash of the password.
- `check_password()` compares the stored hash to a password input, returning `True` if they match.

---

### 4. **Authenticating to a Database Using Environment Variables**

   Using environment variables for database credentials is a security best practice to avoid hardcoding sensitive information in code. Here's a simple example with `psycopg2` for a PostgreSQL database:

   ```python
   import os
   import psycopg2
   from psycopg2 import sql

   # Load environment variables
   db_name = os.getenv("DB_NAME")
   db_user = os.getenv("DB_USER")
   db_password = os.getenv("DB_PASSWORD")
   db_host = os.getenv("DB_HOST", "localhost")  # Default to localhost if not set

   # Connect to the database
   try:
       connection = psycopg2.connect(
           dbname=db_name,
           user=db_user,
           password=db_password,
           host=db_host
       )
       print("Connected to the database successfully!")
   except Exception as e:
       print(f"Error connecting to the database: {e}")
   finally:
       if connection:
           connection.close()
   ```

- **Environment Variables**: Set `DB_NAME`, `DB_USER`, `DB_PASSWORD`, and `DB_HOST` in your environment.
- **Connecting Securely**: By reading sensitive values from environment variables, you reduce the risk of accidental exposure.
