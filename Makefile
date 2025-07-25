run:
	@uv run uvicorn workout_api.main:app --reload

migrations:
	@set PYTHONPATH=%PYTHONPATH%;%CD% && alembic revision --autogenerate -m $(d)


migrate:
	@set PYTHONPATH=%PYTHONPATH%;%CD% && alembic upgrade head
