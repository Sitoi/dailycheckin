.PHONY: build up stop pull logs down exec

build:
	docker-compose build --no-cache
up:
	docker-compose up -d
stop:
	docker-compose stop
down:
	docker-compose down
pull:
	docker-compose pull
logs:
	docker-compose logs -f
exec:
	docker exec -it dailycheckin sh