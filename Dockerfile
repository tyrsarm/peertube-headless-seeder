# Use an official Python runtime as the base image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY pip_requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r pip_requirements.txt

# Copy the scripts and make them executable
COPY main.py .
RUN chmod +x main.py
COPY apipoll.py .
RUN chmod +x apipoll.py
COPY get_url.py .
RUN chmod +x get_url.py
COPY playlive.py .
RUN chmod +x playlive.py

# Copy txt files (used for variables between the scripts)
COPY isPlaying.txt .
COPY isLive.txt .
COPY new_id.txt .
COPY url_file.txt .

# Install Firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends firefox
#RUN apt-get update && apt-get install -y firefox

# Set the environment variable
ENV api_url="https://jupiter.tube/api/v1/accounts/jblive/videos"

# Run the script
CMD [ "python", "./main.py" ]
