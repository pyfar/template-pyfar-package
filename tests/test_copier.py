import pytest

def test_project_folder(copie, copier_project_defaults):
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)

    assert project.exit_code == 0
    assert project.exception is None
    assert project.project_dir.is_dir()


@pytest.mark.parametrize("file_name", [
    "README.md",
])
def test_generated_file_exists(copie, copier_project_defaults, file_name):
    # Create a project
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)

    # Test generated files
    assert project.project_dir.joinpath(file_name).exists()


def test_readme(copie, copier_project_defaults):
    # Create a project
    project_defaults = copier_project_defaults
    project = copie.copy(extra_answers=project_defaults)

    # Test README.md file content
    content = project.project_dir.joinpath("README.md").read_text()
    string = "pip install " + project_defaults['project_slug']
    long_description = project_defaults['project_long_description']

    assert 'https://circleci.com/gh/pyfar/my-project' in content
    assert string in content
    assert long_description in content

