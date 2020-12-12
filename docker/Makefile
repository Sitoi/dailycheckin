.PHONY: build up stop pull logs rm exec

build:
	docker-compose build --no-cache
up:
	docker-compose up -d
stop:
	docker-compose stop
rm: stop
	docker-compose rm
pull:
	docker-compose pull
logs:
	docker-compose logs -f
exec:
	docker exec -it dailycheckin sh