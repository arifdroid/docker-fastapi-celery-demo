docker-compose run app alembic revision --autogenerate -m "New Migration" docker-compose run app alembic upgrade head

docker-compose build docker-compose up