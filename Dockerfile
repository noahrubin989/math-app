# Use the official Python 3.11.x image as a base
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the files required for the app into the container
COPY app.py .
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port where Streamlit runs the app
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]