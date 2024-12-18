FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the model and application files

COPY . .

# Install necessary packages
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 5000

CMD ["python", "train.py"]

# Run the application
CMD ["python", "app.py"]
