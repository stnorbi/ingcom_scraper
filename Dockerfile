FROM python:3.8

COPY . /tmp/IngCom_scraper/
WORKDIR /tmp/IngCom_scraper
RUN pip install -r requirements.txt

CMD ["python3", "main.py"]
