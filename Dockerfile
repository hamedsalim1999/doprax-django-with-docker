# main image
FROM python:3.7

# options
ENV PYTHONUNBUFFERED 1

# Set working directory
RUN mkdir /resume
# set working directory
WORKDIR /resume
# coppy commands 
COPY . /resume

# Installing requirements
ADD requirements.txt /resume
# run commnad  for install 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Collect static files
RUN python core/manage.py collectstatic --no-input

# migrations command
RUN python core/manage.py makemigrations
RUN python core/manage.py migrate

CMD ["gunicorn", "--chdir", "resume", "--bind", ":8000", "core.wsgi:application"]