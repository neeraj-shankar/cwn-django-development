What are mixin in Django Rest Framework?
-----------------------------------------------------------------------------------------------------------------------
Mixins in Django Rest Framework (DRF) are a way to reuse and share common behavior among views. 

They provide a modular and reusable approach to adding functionalities to views without having to duplicate code. Mixins are 
often used to encapsulate common patterns for operations like authentication, permissions, and serialization.


Why Mixins are useful?
-----------------------------------------------------------------------------------------------------------------------
Suppose you have a model called Book: 

Now, let's say you want to create a DRF view that allows users to list all books, retrieve a specific book by its ID, 
create a new book, update an existing book, and delete a book.

