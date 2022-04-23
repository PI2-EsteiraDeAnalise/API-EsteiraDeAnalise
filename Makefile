run:
	docker-compose up -d --remove-orphans
	docker exec api-esteiradeanalise_api_1 chmod +x ./flask_db.sh
	docker exec api-esteiradeanalise_api_1 ./flask_db.sh

stop:
	docker-compose down
