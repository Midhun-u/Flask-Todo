ARG python_version=python:3.13-slim

FROM ${python_version}

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python" , "./src/app.py"]