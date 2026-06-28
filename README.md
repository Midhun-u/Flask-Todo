# Flask Todo Backend Server
It's a todo list backend server for learning how to build a backend server from scratch using Python and Flask framework. It is majorly for learning Python and Flask framework for build backend server.

# Features
* Users can sign using their fullname, email and password.
* Users can check their profile.
* Users can create, read, update and delete their todos.

# System Features
* Implemented JWT(Json Web Token) token based authentication and authorization.
* Implemented pagination for fast and effecient reading of data.
* Implemented containerization for easy to deploy server using Docker.
* Modularized using MVC architecture.

# Technologies
* Python
* Flask
* SQLModel
* Postgresql
* Git and Github
* Docker
* MVC architecture
* JWT (Json Web Token)
* Bcrypt

# Installation

### Installing Project
```bash
git clone https://github.com/Midhun-u/Flask-Todo.git
cd Flask-Todo
# Make sure you add .env file and add environment variables.
```

### Creating and activating environment
```bash
python -m venv env

# MacOS / Linux
source ./env/bin/activate 

# Windows (PowerShell)
.\env\Scripts\Activate.ps1 
```

### Installing packages and running server
```bash
pip install -r requirements.txt
python ./src/app.py
```

### Running container
```bash
sudo docker build -t server ./
sudo docker run --network=host server
```