FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-rus && \
    apt-get clean
CMD [ "python", "./main.py" ]
