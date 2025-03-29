# Project Manager

A simple Streamlit application to manage projects. This application allows you to:

- View existing projects and their directory structure
- Create new projects (creates a directory and initializes a git repository)
- Delete existing projects (removes the directory and all its contents)

# Installation

## Option 1: Docker Deployment (Recommended)

#### Prerequisites
- Docker and Docker Compose installed on your system

#### Quick Start with Pre-built Image

The simplest way to run this application is using our pre-built Docker image from GitHub Container Registry:

1. Create a docker-compose.yml file:
```yaml
services:
  streamlit-app:
    image: ghcr.io/bmj2728/pyprojman:latest
    container_name: project-manager
    restart: unless-stopped
    ports:
      # Map container port 8501 to host port 8501 (can be changed)
      - "8501:8501"
    volumes:
      # Map local projects directory to container projects directory
      - "./projects:/app/projects"
```

2. Update the volume path in the docker-compose.yml:
   - Replace `"./projects"` with the actual path on your system where you want to store projects
   - For example: `"/home/username/projects"`

3. Start the container:
```
docker-compose up -d
```

4. Access the application at http://localhost:8501


## Option 2: Local Installation

1. Clone this repository:
```
git clone https://github.com/bmj2728/project-manager-streamlit.git
cd project-manager-streamlit
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Make sure git is installed on your system (required by GitPython):
```
# Ubuntu/Debian
sudo apt-get install git

# CentOS/RHEL
sudo yum install git

# macOS (using Homebrew)
brew install git

# Windows
# Download from https://git-scm.com/download/win
```

4. Run the Streamlit application:
```
streamlit run app.py
```

#### Building Your Own Image (Alternative)

If you prefer to build the image yourself:

```
# Clone the repository
git clone https://github.com/bmj2728/project-manager-streamlit.git
cd project-manager-streamlit

# Build the image
docker build -t project-manager:latest .

# Update your docker-compose.yml to use your local image
# image: project-manager:latest
```

## Usage

1. Open your web browser and navigate to http://localhost:8501 (or the port you configured).

2. Use the sidebar to create or delete projects.

## Features

### Viewing Projects
- The main area displays all existing projects in a grid layout
- For each project, you can see its directories and files
- The `.git` directory is hidden from view

### Creating Projects
- Enter a project name in the sidebar
- Click "Create Project" to create a new project directory and initialize a git repository

### Deleting Projects
- Select a project from the dropdown in the sidebar
- Confirm deletion by checking the confirmation box
- Click "Delete Project" to remove the selected project

## Project Structure

- `app.py`: Main Streamlit application
- `requirements.txt`: List of required Python packages
- `Dockerfile`: Instructions for building the Docker image
- `docker-compose.yml`: Configuration for Docker deployment
- `projects/`: Directory containing all projects (created on first run)

## Requirements

- Python 3.7+
- Streamlit
- GitPython
- Git (system dependency)

## Docker Image Details

The Docker image is available at `ghcr.io/bmj2728/pyprojman:latest` and includes:
- Python 3.9
- Git (required by GitPython)
- All Python dependencies specified in requirements.txt

The image uses a multi-stage build approach for smaller, more efficient containers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 