<h1 align="center">
<!-- <img src="https://github.com/pyfar/gallery/raw/main/docs/resources/logos/pyfar_logos_fixed_size_pyfar.png" width="300"> -->
</h1><br>

# Template for pyfar packages

[![PyPI version](https://badge.fury.io/py/template_pyfar_package.svg)](https://badge.fury.io/py/template_pyfar_package)
[![Documentation Status](https://readthedocs.org/projects/template-pyfar-package/badge/?version=latest)](https://template-pyfar-package.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/pyfar/template-pyfar-package.svg?style=shield)](https://circleci.com/gh/pyfar/template-pyfar-package)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/pyfar/gallery/main?labpath=docs/gallery/interactive/pyfar_introduction.ipynb)

## Overview

This template is used to keep all pyfar packages consistent and provide a good staring point for new packages. It uses [copier](https://copier.readthedocs.io/en/stable/).

## Installation

1. To use this template, first install copier with pip.

    ```console
    pip install copier
    ```

2. Run the following copier command to create a target directory at path_to_target_folder.
   Note: Copier will overwrite files in the given directory if it already exists.

    ```console
    copier copy https://github.com/pyfar/template-pyfar-package path_to_target_folder
    ```


(Requires Python 3.10 or higher)

## Contributing

Check out the [contributing guidelines](https://pyfar.readthedocs.io/en/stable/contributing.html) if you want to become part of pyfar.
