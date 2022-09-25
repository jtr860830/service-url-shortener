PDM = pdm

.PHONY: serve
serve: clean init
	$(PDM) run uvicorn app.main:app --host 0.0.0.0

.PHONY: dev
dev: init
	$(PDM) run uvicorn app.main:app --reload

.PHONY: install
install:
	$(PDM) install

.PHONY: init
init: install
	$(PDM) run alembic upgrade head

.PHONY: test
test: install
	$(PDM) run pytest -vs

.PHONY: clean
clean:
	rm -rf ./__pypackages__/

.PHONY: container
container:
	docker build -f ./docker/Dockerfile -t service-url-shortener .

.PHONY: docker-compose-up
docker-compose-up: container
	docker compose -f ./docker/docker-compose.yml up

.PHONY: docker-compose-down
docker-compose-down:
	docker compose -f ./docker/docker-compose.yml down
