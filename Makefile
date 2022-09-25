PDM = pdm

.PHONY: serve
serve: install
	$(PDM) run uvicorn app.main:app --host 0.0.0.0

.PHONY: dev
dev: install
	$(PDM) run uvicorn app.main:app --reload

.PHONY: install
install:
	$(PDM) install

.PHONY: init
init: install
	$(PDM) run alembic upgrade head
