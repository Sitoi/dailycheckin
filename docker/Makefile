.PHONY: build up stop pull logs down exec buildx pushx

buildx:
	docker buildx build --platform=linux/arm/v6,linux/arm/v7,linux/arm64,linux/amd64 -t sitoi/dailycheckin:latest  .

pushx:
	docker buildx build --platform=linux/arm/v6,linux/arm/v7,linux/arm64,linux/amd64 -t sitoi/dailycheckin:latest  . --push

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