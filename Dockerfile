FROM python:3.11

RUN pip install poetry

COPY . .

RUN poetry install --no-root

EXPOSE 8000

ENTRYPOINT [ "poetry" ,"run", "uvicorn", "sample.main:app", "--host", "0.0.0.0" ]