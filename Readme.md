1. Install Poetry
2. Run `poetry install`
3. Create database with name `postgres-tenant` with user `postgres` and password `postgres`
4. Activate the virtual environment by running `poetry shell`
5. Run `python manage.py migrate`
6. Run `python manage.py runserver`
7. Run following command - 
    ```python
    from app.models import *
    client = Client.objects.create(schema_name='public', name='public')
    domain = Domain.objects.create(tenant=client, domain='localhost', is_primary=True)
    ```
8. Run `python manage.py migrate_schemas`
9. Run `python manage.py createsuperuser`
10. Run `python manage.py runserver`
11. Run to create one more tenancy 
   ```python
   from app.models import *
   client = Client.objects.create(schema_name='bigco', name='bigco')
   domain = Domain.objects.create(tenant=client, domain='bigco.localhost', is_primary=True)
   ```
12. Run `python manage.py migrate_schemas --shared`

Ref Video - https://www.youtube.com/watch?v=uvaO85GbdzA

Note : Use `.localhost` in domain if u want to access admin panel in browser.