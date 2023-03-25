FROM python:3.9
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
RUN export DWAVE_API_TOKEN=${DWAVE_API_TOKEN}
COPY . /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]