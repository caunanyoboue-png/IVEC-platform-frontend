FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend code
COPY ./ivec_project /app/ivec_project
COPY ./apps /app/apps

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]