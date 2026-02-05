import pytest

@pytest.fixture(scope='session')
def copier_project_defaults():
    return {
        "project_slug": "my_project",
        "project_long_description": "my_project_description",
        "project_getting_started": "This is how to get started.",
        "git_username": "pyfar",
        "minimum_python_version": "'3.11'",
        "license": "MIT",
        "copyright_statement": "2025, The pyfar developers",
        "project_short_description": "my_project_short_description",
        }

@pytest.fixture(scope="session")
def default_project(copie_session, copier_project_defaults):
    project = copie_session.copy(
        extra_answers=copier_project_defaults)
    return project
