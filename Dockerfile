FROM python:3.10-slim

# Setup env
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

WORKDIR /app
COPY . .

## Install Firefox
RUN apt update && \
    apt install -y --no-install-recommends firefox-esr

# Install python dependencies
RUN pip install -r requirements.txt --no-cache-dir

# Add a non-root user to run our program
RUN groupadd -r user && \
    useradd --no-log-init -r -g user user && \
    chown -R user:user /app
USER user

ENV peertube_url="https://jupiter.tube/"
ENV ping_interval=300

# Run the script
CMD [ "python", "./main.py" ]
