# pull official base image
FROM python:3.12.4-alpine

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip==24.1.1
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn

# copy project
COPY . .

RUN python manage.py collectstatic --noinput

CMD ["python" "manage.py" "runserver"]