FROM python:3.12.2-bookworm
WORKDIR /URL-shortener
COPY requirements.txt .
RUN pip install --no-cache-dir --use-pep5 -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python3", "create_db.py";"gunicorn", "wsgi:app", "-b", "0.0.0.0:80"]
