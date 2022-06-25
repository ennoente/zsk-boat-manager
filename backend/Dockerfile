FROM python:buster

COPY . .

RUN chmod +x ./wait-for-it.sh

RUN pip install -r requirements.txt

CMD [ "uvicorn", "api:app", "--host=0.0.0.0", "--reload" ]
