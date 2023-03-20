FROM python:3.9
WORKDIR /app
RUN pip install --no-cache-dir --upgrade fastapi uvicorn pydantic
COPY . /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]