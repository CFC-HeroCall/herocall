FROM python:3.9.4
ENV PYTHONUNBUFFERED 1

COPY . .
RUN pip3 install -r requirements.txt

WORKDIR /heroweb

ENV PORT 8000
EXPOSE 8000

CMD ["python", "manage.py", "start"]