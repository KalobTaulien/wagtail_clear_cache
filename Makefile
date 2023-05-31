lint:
	@echo "Linting..."
	flake8 .
	isort .
	black .

server:
	@echo "Running server..."
	@python develop_manage.py runserver 0:8000

init-testapp:
	@echo "Initialsing test app..."
	@echo "Migrating database..."
	@python develop_manage.py migrate
	@echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('test', 'test@test.com', 'test')" | python develop_manage.py shell
	@echo "Done"
