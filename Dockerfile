FROM 902904814612.dkr.ecr.ap-south-1.amazonaws.com/flask-ci-cd-application

ENV PORT=5000
EXPOSE $PORT

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
