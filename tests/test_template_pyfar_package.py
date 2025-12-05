import pytest


def test_import_template_pyfar_package():
    try:
        import template_pyfar_package           # noqa
    except ImportError:
        pytest.fail('import template_pyfar_package failed')
