PDM = pdm

serve: install
	$(PDM) run uvicorn app.main:app --host 0.0.0.0

dev: install
	$(PDM) run uvicorn app.main:app --reload

install:
	$(PDM) install
