# Features
  User Registration: Allow users to create new accounts by providing necessary details like username, email, and password.
  User Login: Enable users to log in using their credentials to access authenticated endpoints.
  User Logout: Provide an endpoint to invalidate user tokens and log them out of the system securely.
  Token-based Authentication: Use JSON Web Tokens (JWT) for token-based authentication, providing a stateless and secure user management system.
  Customizable: Easily extend the API to add more features like profile management, password reset, email verification, etc.


# Authentication
This API uses JSON Web Tokens (JWT) for authentication. Upon successful login, the API will return a JWT token that 
should be included in the Authorization header for protected endpoints. Tokens are valid for a configurable amount of time (e.g., 5 minutes)
and need to be refreshed after expiration.


Prerequisites
Make sure you have the following installed:

Python (>=3.6)
Django (>=3.2)
Django Rest Framework (>=3.12)
and mentioned as requirement.txt
