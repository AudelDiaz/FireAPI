tests:
	docker-compose exec fireapi pip install pytest coverage
	docker-compose exec fireapi python -m coverage run -m pytest --disable-warnings
	docker-compose exec fireapi python -m coverage report -m
	docker-compose exec fireapi python -m coverage html
