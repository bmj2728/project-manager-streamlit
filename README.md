# Project Manager

A simple Streamlit application to manage projects. This application allows you to:

- View existing projects and their directory structure
- Create new projects (creates a directory and initializes a git repository)
- Delete existing projects (removes the directory and all its contents)

## Installation

### Option 1: Local Installation

1. Clone this repository:
```
git clone <repository-url>
cd <repository-directory>
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

### Option 2: Docker Deployment

#### Prerequisites
- Docker and Docker Compose installed on your system

#### Separated Build and Deploy Workflow

##### Build Stage
Build the Docker image:
```
# Use the build script (recommended)
./build.sh

# Or build manually
docker build --no-cache -t project-manager:latest .
```

This creates a Docker image with the tag `project-manager:latest` that can be deployed using docker-compose.

##### Deploy Stage
Deploy the pre-built image using docker-compose:
```
docker-compose up -d
```

This approach properly separates the build process from deployment, allowing you to:
- Build once, deploy multiple times
- Build on one system, deploy on another
- Version and tag your images for different environments

#### Customization

You can customize the deployment by creating a `.env` file based on the provided `.env.example`:

```
cp .env.example .env
```

Then edit the `.env` file to set:
- `STREAMLIT_PORT`: The port on which Streamlit will be accessible (default: 8501)
- `PROJECTS_DIR`: The directory on the host machine to store projects (default: ./projects)

Example:
```
STREAMLIT_PORT=9000
PROJECTS_DIR=/home/user/my-projects
```

After modifying the `.env` file, restart the container:
```
docker-compose down
docker-compose up -d
```

## Usage

1. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501).

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

## Docker Build Details

The Dockerfile uses a multi-stage build approach:

1. **Build Stage**: Installs all dependencies in an isolated environment
2. **Runtime Stage**: Copies only necessary files from the build stage to minimize the final image size

The Docker image includes:
- Python 3.9
- Git (required by GitPython)
- All Python dependencies specified in requirements.txt

This approach results in a smaller, more efficient container. 