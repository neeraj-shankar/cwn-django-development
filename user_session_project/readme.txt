Django Athentication Overview
-----------------------------------------------------------------------------------------------------------------------
The Django authentication system handles both authentication and authorization. 

Briefly, authentication verifies a user is who they claim to be, and authorization determines what an authenticated 
user is allowed to do.

The auth system consists of:

1. Users
2. Permissions: Binary (yes/no) flags designating whether a user may perform a certain task.
3. Groups: A generic way of applying labels and permissions to more than one user.
4. A configurable password hashing system
5. Forms and view tools for logging in users, or restricting content
6. A pluggable backend system


Using the Django authentication system
-----------------------------------------------------------------------------------------------------------------------
User objects are the core of the authentication system. The primary attributes of the default user are:

1. username
2. password
3. email
4. first_name
5. last_name



