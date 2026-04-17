import pytest

@pytest.fixture(scope='session')
def copier_project_defaults():
    return {
        "project_slug": "my-project",
        "project_long_description": "my_project_description",
        "project_getting_started": "This is how to get started.",
        "project_installation_instructions": "Installation instructions.",
        "additional_section_readme": "## Section\n\nSection description.",
        "git_username": "pyfar",
        "minimum_python_version": "3.11",
        "license": "MIT",
        "copyright_statement": "2025, The pyfar developers",
        "project_short_description": "my_project_short_description",
        "python_versions": "['3.9', '3.10', '3.11', '3.12', '3.13', '3.14']",
        "manifest_custom": "recursive-include your/custom/path/,"
        "recursive-exclude another/custom/path/'",
        "docs_custom_import": "module, anothermodule",
        "add_submodules": "true",
        "submodule_path": "path/to/submodule",
        "introduction_path": "docs/gallery/interactive/"
        "pyfar_introduction.ipynb",
        }

@pytest.fixture(scope="session")
def default_project(copie_session, copier_project_defaults):
    project = copie_session.copy(
        extra_answers=copier_project_defaults)
    return project
