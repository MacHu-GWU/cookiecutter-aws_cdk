# -*- coding: utf-8 -*-

from {{ cookiecutter.package_name }}.one.one_01_config import OneConfigMixin

from {{ cookiecutter.package_name }}.config.api import Config
from {{ cookiecutter.package_name }}.one.api import One


def test_config():
    one = One()
    assert isinstance(one, OneConfigMixin)
    assert isinstance(one.config, Config)
    assert one.config.project_name == "{{ cookiecutter.package_name }}"
    assert one.config.env_name == one.env.current_env_name
    # cached: built once
    assert one.config is one.config


if __name__ == "__main__":
    from {{ cookiecutter.package_name }}.tests import run_cov_test

    run_cov_test(
        __file__,
        "{{ cookiecutter.package_name }}.one.one_01_config",
        preview=False,
    )
