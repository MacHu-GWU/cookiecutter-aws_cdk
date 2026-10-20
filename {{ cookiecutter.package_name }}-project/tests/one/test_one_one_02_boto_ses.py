# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.one.one_02_boto_ses import OneBotoSesMixin


def test():
    """
    Placeholder: the session logic is a few lines with nothing worth testing yet.
    """
    _ = OneBotoSesMixin


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.one.one_02_boto_ses",
        preview=False,
    )
