import pytest

@pytest.fixture(scope="session")
def default_project(copie_session, copier_project_defaults):
    project = copie_session.copy(
        extra_answers=copier_project_defaults)
    return project

def test_project_folder(default_project):
    assert default_project.exit_code == 0
    assert default_project.exception is None
    assert default_project.project_dir.is_dir()


@pytest.mark.parametrize("file_name", [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.rst",
])
def test_generated_file_exists(default_project, file_name):
    assert default_project.project_dir.joinpath(file_name).exists()


@pytest.mark.parametrize("desired", [
    "\nmy_project_description\n",
    "pip install my_project",
    "https://circleci.com/gh/pyfar/my-project",
    "main/docs/resources/logos/pyfar_logos_fixed_size_my_project.png",
    "Python 3.11 or higher",
    "py/my_project.svg",
    "https://my_project.readthedocs.io/en/stable/contributing.html",
    "\nThis is how to get started.\n",
])
def test_content_readme(default_project, desired):
    content = default_project.project_dir.joinpath("README.md").read_text()
    assert desired in content


def test_license_default(default_project):
    content = default_project.project_dir.joinpath("LICENSE").read_text()
    assert 'Copyright (c) 2025, The pyfar developers' in content


@pytest.mark.parametrize(("license_default", "desired"), [
    ("MIT", "The MIT License (MIT)"),
    ("BSD-3-Clause", "Redistribution and use in source and binary forms"),
    ("Apache-2.0", "Apache License"),
    ("GPL-3.0-only", "GNU GENERAL PUBLIC LICENSE"),
    ("EUPL-1.2", "EUROPEAN UNION PUBLIC LICENCE v. 1.2"),
    ("MPL-2.0", "Mozilla Public License Version 2.0")])
def test_content_license(copie, copier_project_defaults,
                                 license_default, desired):
    project = copie.copy(extra_answers={**copier_project_defaults,
                                         "license": license_default})
    content = project.project_dir.joinpath("LICENSE").read_text()
    assert desired in content


def test_license_choice_other(copie, copier_project_defaults):
    project = copie.copy(extra_answers={**copier_project_defaults,
                                         "license": ""})
    assert not project.project_dir.joinpath("LICENSE").exists()


@pytest.mark.parametrize("desired", [
    "https://github.com/pyfar/my_project/issues",
    "$ cd my_project",
])
def test_content_contributing(default_project, desired):
    content = default_project.project_dir.joinpath(
                                    "CONTRIBUTING.rst").read_text()
    assert desired in content
