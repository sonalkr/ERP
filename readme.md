```/ERP
    /app
        __init__.py
        main.py
        /routers
            __init__.py
            users.py
            items.py
        /models
            __init__.py
            users.py
            items.py
        /schemas
            __init__.py
            users.py
            items.py
    /tests
        test_main.py
        /test_routers
            test_users.py
            test_items.py
    .env
    .gitignore
    README.md
    requirements.txt
```

## how to run

Navigate to your project directory and activate your virtual environment:

`cd ERP`
`source env/bin/activate`

# On Windows, use `env\Scripts\activate`

Then, run your FastAPI application with Uvicorn:

`uvicorn app.main:app --reload`

This command tells Uvicorn to import an application instance (app) from your main.py file in the app directory. The --reload flag enables hot reloading, which means the server will automatically update whenever you make changes to your code.

You should now be able to access your FastAPI application at http://localhost:8000/.

If your application is running at http://localhost:8000/, you can access the Swagger UI (OpenAPI) documentation at http://localhost:8000/docs.

database migration

`alembic revision --autogenerate -m "Initial migration"`

`alembic upgrade head`
