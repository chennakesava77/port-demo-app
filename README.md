## Project-title port demo app

## project over view
This project demonstrates a minimal production-ready web application built with Python FastAPI.
containerized using Docker, orchestrated with Docker Compose, and automated using a GitHub Actions CI pipeline.

-->The main focus of this project is to clearly explain ports and networking in Docker.
   including how traffic flows from the browser to the containerized application.

   ## Technologys:
   1.language:python 3.11
   2.frame work: fast API
   3.Containerization: Docker
   4.Orchestration: Docker Compose
   5.CI/CD: GitHub Actions
   6.Registry: Docker Hub
   ## Application Requirements (Implemented):
   The application:Starts an HTTP server 
   Exposes two endpoints:/ → returns:
  - application name
   -port the app is listening on
   -/health → returns health status
   -Reads the listening port from an environment variable (APP_PORT)
   ## End Points:
   /:Returns app name and port
   /health:Health check endpoint

  example:{
  "app_name": "Port Demo App",
  "port": "8000"
}

*In With out docker I am Creating Virtual environment
 python3 -m venv venv

 * after i activated my virtual environment
   source venv/bin/activate

  * next insall all requirements
    pip install -r requirements.txt

   * after i am doing Set port environment variable
     export APP_PORT=8000

   * Next run the app by using these command
     uvicorn app.main:app --host 0.0.0.0 --port $APP_PORT

   *I will check my app is running and app health by using port
       curl http://localhost:8000/
       curl http://localhost:8000/health

       <img width="1920" height="1080" alt="Screenshot (17)" src="https://github.com/user-attachments/assets/2b63bb66-afa6-4e40-a9b6-2f2bcd12e034" />


   *next run the docker with single container to create docker image
      docker build -t port-demo-app .

    *next run container
     docker run -d \
     -e APP_PORT=8000 \
     -p 9090:8000 \
     --name port-demo \
      port-demo-app

   * after i wiill check my container status and health
      curl http://localhost:9090/
      curl http://localhost:9090/health

   * next  i am doing docker compose build  to start the application
       docker compose up --build -d
   * now stop the container
     docker compose down
## Traffic Flow
Browser
  ↓ http://localhost:9090
Host Machine (9090)
  ↓ Docker port mapping
Container (8000)
  ↓
FastAPI Application

## Project Structure
port-demo-app/
├── app/
│   ├── __init__.py
│   └── main.py
│
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── venv/               # (local only, not committed ideally)

## Architecture Diagram

flowchart TD
    User[User] -->|HTTP Request: HostPort 8000| Host[Host Machine]
    Host -->|Docker Port Mapping: HostPort 8000 → ContainerPort 5000| DockerCompose[Docker Compose]
    DockerCompose --> AppContainer[Application Container]
    AppContainer -->|App listens on $APP_PORT (5000)| App[FastAPI/Express App]
    App -->|Response /health, /| User

    subgraph Notes
        note1["Host Port: 8000 (accessible from browser)"]
        note2["Container Port: 5000 (internal app port)"]
        note3["App reads port from environment variable $APP_PORT"]
    end

    Host --- note1
    AppContainer --- note2
    App --- note3


(https://github.com/user-attachments/assets/b01b910c-d427-4ee1-81da-60f41e7009e0)






   



 

   















    
    


