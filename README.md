# Buck Online Card Game
This is the code to run a Django web server running buck.

Run with `python django/manage.py runserver`
Run in Docker with `docker exec -d buck-dev python3 /debugpy/launcher host.docker.internal:57948 -- django/manage.py runserver 0.0.0.0:8000 --nothreading --noreload`

# Setup
For Django and Docker setup, you can follow https://code.visualstudio.com/docs/python/tutorial-django and https://code.visualstudio.com/docs/containers/quickstart-python respectively