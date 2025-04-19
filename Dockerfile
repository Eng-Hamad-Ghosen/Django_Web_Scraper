FROM python:3.11.4-alpine

WORKDIR /usr/src/app

# prevent python from writing .pyc files
#لحتى امنع البايثون من التعامل مع ملفات ال.pyc
ENV PYTHONDONTWRITEBYTECODE=1


ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --default-timeout=100 --no-cache-dir -r /usr/src/app/requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]