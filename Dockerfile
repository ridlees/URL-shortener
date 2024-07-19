FROM python:3.12.2-bookworm
WORKDIR /URL-shortener
COPY . .
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
RUN python ./create_db.py
COPY . .
EXPOSE 80
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:80"]
