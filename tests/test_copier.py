import pytest
from datetime import date

def test_project_folder(default_project):
    assert default_project.exit_code == 0
    assert default_project.exception is None
    assert default_project.project_dir.is_dir()


@pytest.mark.parametrize("file_name", [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.rst",
    "pyproject.toml",
    "my_project/__init__.py",
    "my_project/my_project.py",
    "HISTORY.rst",
    ".github/workflows/check_modified_history.yml",
    "docs/modules/my_project.rst",
    "docs/my_project.rst",
    "docs/api_reference.rst",
    "docs/conf.py",
    "docs/contributing.rst",
    "docs/history.rst",
    "docs/index.rst",
    "docs/make.bat",
    "docs/Makefile",
    "docs/readme.rst",
    "MANIFEST.in",
    ".readthedocs.yml",
    ".copier-answers.yml",
    ".editorconfig",
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


@pytest.mark.parametrize("desired", [
    'name = "my_project"',
    'version = "0.1.0"',
    'description = "my_project_short_description"',
    'requires-python = ">=3.11"',
    '\n    "acoustics",\n',
    '\n    "pyfar",\n',
    '\n    "numpy",\n',
    '\n    "scipy",\n',
    '"License :: OSI Approved :: MIT License"',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    'Programming Language :: Python :: 3.13',
    'Programming Language :: Python :: 3.14',
    'Tracker = "https://github.com/pyfar/my_project/issues"',
    '"docs",\n    "examples/",',
])
def test_content_pyproject(default_project, desired):
    content = default_project.project_dir.joinpath(
                                        "pyproject.toml").read_text()
    assert desired in content, f"{desired!r} is not in content"


@pytest.mark.parametrize("not_desired", [
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
])
def test_incorrect_content_pyproject(default_project, not_desired):
    content = default_project.project_dir.joinpath(
                                        "pyproject.toml").read_text()
    assert not_desired not in content, f"{not_desired!r} is in content"


@pytest.mark.parametrize("desired", [
    'Top-level package for my_project.',
    '__author__ = """The pyfar developers"""',
    "__version__ = '0.1.0'",
])
def test_content_project_slug_init(default_project, desired):
    content = default_project.project_dir.joinpath('my_project').joinpath(
                                        "__init__.py").read_text()
    assert desired in content, f"{desired!r} is not in content"


def test_content_history(default_project):
    content = default_project.project_dir.joinpath(
                                    "HISTORY.rst").read_text()
    desired = f"0.1.0 ({date.today().strftime('%Y-%m-%d')})"
    assert desired in content


@pytest.mark.parametrize("desired", [
    "project = 'my_project'",
    'copyright = "2025, The pyfar developers"',
    'author = "The pyfar developers"',
    "'numpy': ('https://numpy.org/doc/stable/', None)",
    '\n     "index": "my_project.html"',

])
def test_content_docs_conf(default_project, desired):
    content = default_project.project_dir.joinpath('docs/conf.py').read_text()
    assert desired in content, f"{desired!r} is not in content"


@pytest.mark.parametrize("file_name", [
    'docs/modules/my_project.rst',
    'docs/my_project.rst',
    'docs/api_reference.rst',
    'docs/index.rst',
    'docs/make.bat',
    'docs/Makefile',
])
def test_content_docs_multiple_files(default_project, file_name):
    content = default_project.project_dir.joinpath(file_name).read_text()
    desired = "my_project"
    assert desired in content, f"{desired!r} is not in content"


@pytest.mark.parametrize("desired", [
    '- libsndfile1',
    "python: 3.14",
])
def test_content_readthedocs(default_project, desired):
    content = default_project.project_dir.joinpath(
                                    ".readthedocs.yml").read_text()
    assert desired in content
