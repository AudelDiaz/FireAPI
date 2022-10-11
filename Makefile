tests:
	docker-compose exec fireapi pip install pytest
	docker-compose exec fireapi python -m pytest --disable-warnings
