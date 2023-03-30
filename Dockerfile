FROM python:slim

WORKDIR /app

# Copy necessary files
COPY *.txt *.py ./

# Install python dependencies
RUN pip install --no-cache-dir -r pip_requirements.txt

# Install Firefox
ENV DEBIAN_FRONTEND=noninteractive
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends firefox && \
    rm -rf /var/lib/apt/lists/*

# Add a non-root user to run our program
RUN groupadd -r myuser && useradd --no-log-init -r -g myuser myuser && chown -R myuser:myuser /app
USER myuser

# Set the environment variable
ENV api_url="https://jupiter.tube/api/v1/accounts/jblive/videos"

# Run the script
CMD [ "python", "./main.py" ]
