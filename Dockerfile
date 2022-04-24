FROM python:3.8

COPY . /tmp/IngCom_scraper/
WORKDIR /tmp/IngCom_scraper

# Copy the file from the local host to the filesystem of the container at the working directory.
COPY requirements.txt ./
 
# Install Scrapy specified in requirements.txt.
RUN pip3 install --no-cache-dir -r requirements.txt
 
# Copy the project source code from the local host to the filesystem of the container at the working directory.
COPY . .

CMD ["python3", "./run_scraper.py"]
