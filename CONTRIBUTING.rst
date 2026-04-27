.. highlight:: shell

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given. The following helps you to start
contributing specifically to template-pyfar-package. Please also consider the
`general contributing guidelines`_ for example regarding the style
of code and documentation and some helpful hints.

Types of Contributions
----------------------

Report Bugs or Suggest Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The best place for this is https://github.com/pyfar/template-pyfar-package/issues.

Fix Bugs or Implement Features
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look through https://github.com/pyfar/template-pyfar-package/issues for bugs or feature requests
and contact us or comment if you are interested in implementing.

Write Documentation
~~~~~~~~~~~~~~~~~~~

template-pyfar-package could always use more documentation, whether as part of the
official template-pyfar-package docs, in docstrings, or even on the web in blog posts,
articles, and such.

Get Started!
------------

Ready to contribute? Here's how to set up `template-pyfar-package` for local development using the command-line interface.
Note that several alternative user interfaces exist, e.g., the Git GUI, `GitHub Desktop <https://desktop.github.com/>`_,
extensions in `Visual Studio Code <https://code.visualstudio.com/>`_ ...

1. `Fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo/>`_ the `template-pyfar-package` repo on GitHub.
2. Clone your fork locally and cd into the template-pyfar-package directory::

    $ git clone https://github.com/YOUR_USERNAME/template-pyfar-package.git
    $ cd template-pyfar-package

3. Install your local copy into a virtualenv. Assuming you have Anaconda or Miniconda installed, this is how you set up your fork for local development::

    $ conda create --name template-pyfar-package python
    $ conda activate template-pyfar-package
    $ pip install -e ".[dev]"

4. Create a branch for local development. Indicate the intention of your branch in its respective name (i.e. `feature/branch-name` or `bugfix/branch-name`)::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass ruff and the
   tests::

    $ ruff check
    $ pytest

   ruff must pass without any warnings for `./template-pyfar-package` and `./tests` using the default or a stricter
   configuration. Ruff ignores a couple of PEP Errors (see `./pyproject.toml`). If necessary, adjust your linting configuration in your IDE accordingly.

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request on the develop branch through the GitHub website.

.. _general contributing guidelines: https://pyfar-gallery.readthedocs.io/en/latest/contribute/index.html
