# Financial Assistant

This application is designed to automate the processing and querying of W-2 forms. Utilizing Veryfi API for OCR capabilities, the system extracts data from uploaded W-2 documents and stores this information securely. For interactive querying, the system integrates OpenAI's Assistants API, allowing users to ask questions and receive intelligent responses based on the extracted W-2 data.

## Features

- **Document Parsing**: Users can upload W-2 forms, which are then processed to extract data using Veryfi API.
- **Interactive Querying**: Leverage OpenAI's Assistants API to enable users to ask questions and get insights about the parsed W-2 data.
- **User Authentication**: Implements a secure authentication system to manage user access and protect sensitive information.
- **Docker Integration**: Fully containerized application setup for easy development and deployment.
- **Secure Data Handling**: Ensures that all personal information, especially Social Security Numbers, are handled securely with partial masking techniques.

## Prerequisites

Before you begin, ensure you have the following installed:
- Docker and Docker Compose
- NodeJS and Angular CLI

## Project Setup

### Backend Setup
#### Step 1: Create Environment Variables
Create a `.env` file by copying the `.env.example` file provided in the repository. Adjust the environment variables as necessary to match your setup, particularly your API keys.

#### Step 2: Build and Run with Docker
For the initial setup, build and run the Docker containers using the command:

``` bash 
docker compose up --build
```

For subsequent runs, you can start the application without rebuilding unless changes are made to the dependencies or docker setup:

``` bash 
docker compose up
```
This will start the Flask backend and the PostgreSQL database using Docker containers.

### Frontend Setup
#### Step 1: Clone the Repository
``` bash
git clone https://github.com/44mkashif/financial-assistant-frontend
```

#### Step 2: Install Dependencies
Navigate to the frontend project directory and install dependencies:

``` bash 
npm install
```

#### Step 2: Run the application
Start the frontend application with:

``` bash 
npm start
```

This should open the application in your default web browser, or you can access it at `http://localhost:4200`.

## Using the Application
Once the application is running, you can navigate to http://localhost:4200 in your web browser to upload W-2 forms. The application will parse the uploaded documents using the Veryfi API, and you can interactively query the parsed data using the built-in chat interface.

## Production Deployment
- **Backend**: Hosted on an AWS EC2 instance.
- **Database**: PostgreSQL database hosted on AWS RDS
- **Frontend**: Statically served from an AWS S3 bucket
- **Website Link**: [Financial Assistant Website](http://kashif-financial-assistant.s3-website.us-east-2.amazonaws.com/)

## Dependencies
- **Flask**: Web framework used for the backend.
- **PostgreSQL**: Database used for storing parsed data and application data.
- **SQLAlchemy** ORM & **Psycopg2** PostgreSQL Adapter.
- **Docker & Docker Compose**: For containerization.
- **Angular**: For the frontend framework
- **Veryfi API**: For OCR capabilities to extract data from W-2 forms.
- **OpenAI Assistants API**: For enabling interactive queries on the parsed data.

## Documentation
For more detailed information about the APIs and technologies used, refer to the following resources:

[Veryfi API Documentation](https://docs.veryfi.com/api/w2s/process-a-w-2/)

[OpenAI API Documentation](https://platform.openai.com/docs/assistants/overview)
