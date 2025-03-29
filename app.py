import streamlit as st
import os
import shutil
import git
import time

# Set page configuration
st.set_page_config(
    page_title="Project Manager",
    page_icon="📁",
    layout="wide"
)

# Constants
# Use absolute path for Docker compatibility
PROJECTS_DIR = "/app/projects"

# Create projects directory if it doesn't exist
if not os.path.exists(PROJECTS_DIR):
    os.makedirs(PROJECTS_DIR)

def get_projects():
    """Get a list of all projects in the projects directory."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    
    return [d for d in os.listdir(PROJECTS_DIR) 
            if os.path.isdir(os.path.join(PROJECTS_DIR, d))]

def create_project(project_name):
    """Create a new project directory and initialize git repository."""
    if not project_name:
        return False, "Project name cannot be empty."
    
    # Check if project exists
    project_path = os.path.join(PROJECTS_DIR, project_name)
    if os.path.exists(project_path):
        return False, f"Project '{project_name}' already exists."
    
    try:
        # Create project directory
        os.makedirs(project_path)
        
        # Initialize git repository
        git.Repo.init(project_path)
        
        return True, f"Project '{project_name}' created successfully."
    except Exception as e:
        return False, f"Error creating project: {str(e)}"

def delete_project(project_name):
    """Delete a project directory and all its contents."""
    if not project_name:
        return False, "Project name cannot be empty."
    
    project_path = os.path.join(PROJECTS_DIR, project_name)
    if not os.path.exists(project_path):
        return False, f"Project '{project_name}' does not exist."
    
    try:
        shutil.rmtree(project_path)
        return True, f"Project '{project_name}' deleted successfully."
    except Exception as e:
        return False, f"Error deleting project: {str(e)}"

# Initialize session state
if 'project_created' not in st.session_state:
    st.session_state.project_created = False

# App title
st.title("📁 Project Manager")
st.markdown("Manage your projects with ease. Create new projects or delete existing ones.")

# Sidebar for actions
with st.sidebar:
    st.header("Actions")
    
    # Create new project section
    st.subheader("Create New Project")
    
    # Reset the input if a project was just created
    if st.session_state.project_created:
        new_project_name = st.text_input("Project Name", value="", key="new_project")
        st.session_state.project_created = False
    else:
        new_project_name = st.text_input("Project Name", key="new_project")
    
    create_btn = st.button("Create Project")
    
    if create_btn:
        success, message = create_project(new_project_name)
        if success:
            st.success(message)
            # Mark that a project was created so the input can be reset on next rerun
            st.session_state.project_created = True
            # Add a small delay to allow the success message to be displayed
            time.sleep(0.5)
            st.experimental_rerun()
        else:
            st.error(message)
    
    # Delete project section
    st.subheader("Delete Project")
    projects = get_projects()
    if projects:
        project_to_delete = st.selectbox("Select Project to Delete", projects)
        delete_confirmation = st.checkbox("I understand this action cannot be undone")
        delete_btn = st.button("Delete Project")
        
        if delete_btn:
            if delete_confirmation:
                success, message = delete_project(project_to_delete)
                if success:
                    st.success(message)
                    # Add a small delay to allow the success message to be displayed
                    time.sleep(0.5)
                    st.experimental_rerun()
                else:
                    st.error(message)
            else:
                st.warning("Please confirm deletion by checking the box.")
    else:
        st.info("No projects to delete.")

# Main content area - show projects
st.header("Projects")
projects = get_projects()

if projects:
    # Display projects in a grid layout
    col_count = 3
    cols = st.columns(col_count)
    
    for i, project in enumerate(projects):
        col_idx = i % col_count
        project_path = os.path.join(PROJECTS_DIR, project)
        
        with cols[col_idx]:
            st.markdown(f"### {project}")
            
            # Get some project details
            dirs = []
            files = []
            
            try:
                for item in os.listdir(project_path):
                    item_path = os.path.join(project_path, item)
                    if os.path.isdir(item_path):
                        if item != '.git':  # Don't show .git directory
                            dirs.append(item)
                    else:
                        files.append(item)
            except Exception as e:
                st.error(f"Error reading project: {str(e)}")
            
            # Show directory info
            if dirs:
                st.markdown("**Directories:**")
                for d in dirs:
                    st.markdown(f"- 📁 {d}")
            
            # Show file info
            if files:
                st.markdown("**Files:**")
                for f in files:
                    st.markdown(f"- 📄 {f}")
            
            if not dirs and not files:
                st.info("Empty project")
            
            st.markdown("---")
else:
    st.info("No projects found. Create a new project using the sidebar.")

# Footer
st.markdown("---")
st.markdown("&copy; 2025 Project Manager | Built with Streamlit") 