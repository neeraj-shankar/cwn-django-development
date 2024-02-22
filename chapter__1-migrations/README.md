# Django Migrations
[Django Documentation](https://docs.djangoproject.com/en/5.0/topics/migrations/)

## Migrations Overview
#### Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema.

#### We should think of migrations as a version control system for your database schema. makemigrations is responsible for packaging up your model changes into individual migration files - analogous to commits - and migrate is responsible for applying those to your database

## Migration Command
1. migrate: Responsible for applying and unapplying migrations.
2. makemigrations: Responsible for creating new migrations based one changes made in models file.
3. sqlmigrate: displays the SQL statements for a migration
4. showmigrations: lists a project's migration and their status

## Transactions in Database
-  A transaction refers to a sequence of one or more database operations that are treated as a single logical unit of work. 
- The key properties of transactions are often abbreviated as ACID:
    1. Atomicity: Transactions are atomic, meaning that either all the operations within a transaction are successfully completed, or none of them are.
    2. Consistency: Transactions maintain the consistency of the database. This means that the database transitions from one consistent state to another consistent state after the successful completion of a transaction.
    3. Isolation: Transactions are isolated from each other, meaning that the changes made by one transaction are not visible to other transactions until the transaction is committed.
    4. Durability: Once a transaction is committed, its changes are durable and persistent, even in the event of a system failure or crash. The changes made by committed transactions are permanently stored in the database and remain intact, even if the system is restarted

- We can prevent a migration from running in a transaction by setting the atomic attribute to False.
```
from django.db import migrations

class Migration(migrations.Migration):
    atomic = False
```

## Dependencies
- Dependencies are used to specify the order in which migrations should be applied. 
- Dependencies ensure that migrations are applied in the correct sequence to maintain consistency and integrity of the database schema.

```
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),  # Reference to the migration for the Author model
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.ForeignKey(to='authors.Author', on_delete=models.CASCADE)),
            ],
        ),
    ]

```
### Common Errors when dependenies are not sequenced correctly. 
- ForeignKeyConstraintError: If the Book model includes a foreign key field referencing the Author model, attempting to create the Book model before the Author model exists in the database will result in a ForeignKeyConstraintError.
- TableDoesNotExistError: When the migration for the Book model is applied, it attempts to create the corresponding table in the database. However, if the migration for the Author model has not been applied yet, the database engine will raise a TableDoesNotExistError because it cannot find the referenced table (Author) when creating the foreign key constraint.
- IntegrityError: If there are existing records in the database that violate referential integrity constraints (e.g., orphaned records with invalid foreign key references), attempting to apply the migration for the Book model before resolving these inconsistencies may result in IntegrityError when the database engine attempts to enforce referential integrity
- Inconsistent Database State: Running migrations out of order can leave the database in an inconsistent state where certain tables or columns are missing, foreign key constraints are not properly set up, or data dependencies are violated. This can lead to unexpected behavior, data corruption, or data loss.





