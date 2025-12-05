import pytest

@pytest.fixture(scope='session')
def copier_project_defaults():
    return {
        "project_slug": "my_project",
        "project_long_description": "my_project_description",
        "project_getting_started": "This is how to get started with my_project.",
        "git_username": "pyfar",
        "minimum_python_version": "3.11",
        }
