run:
	docker-compose up -d --build --remove-orphans
	docker-compose logs -f --tail="all"

network:
	docker network create pi2-esteira-network

test:
	docker exec api_esteira chmod +x ./run_pytest.sh
	docker exec api_esteira ./run_pytest.sh

stop:
	docker-compose down
