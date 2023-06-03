# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project code
COPY . .

# Expose the necessary port (e.g., 8000 for Django development server)
EXPOSE 8000

# Set the command to run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
