# Release Notes - Project Manager v0.0.1

## Overview

Initial release of Project Manager, a simple Streamlit application for managing and organizing projects. This tool helps developers maintain multiple project directories with Git integration in a clean, visual interface.

## Features

### Core Functionality
- **Project Browsing**: View all your projects in a clean grid layout
- **Project Creation**: Create new project directories with pre-initialized Git repositories
- **Project Deletion**: Safely remove projects and all their contents
- **File/Directory Visualization**: Browse the file and directory structure of each project

### Technical Features
- **Git Integration**: Automatically initializes Git repositories for new projects
- **Docker Support**: Pre-built Docker image available for easy deployment
- **Clean UI**: Modern Streamlit interface with intuitive navigation
- **Multi-platform**: Works on any system that supports Python or Docker

## Deployment Options

- **Local Installation**: Run directly with Python and Streamlit
- **Docker Deployment**: Deploy using the pre-built image from GitHub Container Registry
  - Image: `ghcr.io/bmj2728/pyprojman:latest`

## Technical Details

- Built with Streamlit 1.22.0
- Python 3.9 base
- GitPython 3.1.30 for Git operations
- Dockerized with multi-stage build for optimized image size

## Requirements

- Python 3.7+ (for local installation)
- Git (system dependency)
- Docker and Docker Compose (for Docker deployment)

## Known Limitations

- Projects are stored in a single parent directory
- Limited to Git repositories only
- Basic file/directory visualization without editing capabilities

## What's Next

Future releases may include:
- Enhanced project templates
- Git operations (commit, push, pull) from the UI
- File editing capabilities
- Project configuration options
- Multiple project directory support

## License

This project is licensed under the MIT License. 