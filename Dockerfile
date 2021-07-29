FROM python:3.8.2-alpine
ENV PYTHONUNBUFFERED 1

COPY . requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /heroweb

ENV PORT 3000
EXPOSE 3000

CMD ["python3", "manage.py", "start"]