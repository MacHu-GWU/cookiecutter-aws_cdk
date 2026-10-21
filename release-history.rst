.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


0.1.1 (2026-10-21)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Built from seed @ ``d4b9e7b``

First release. Generates a multi-environment (``dev``, ``tst``, ``prd``) AWS CDK project in Python.

**Features and Improvements**

- Environment and runtime detection, a JSON5 config per environment (shared, per-environment, and git-ignored secret files), and a project singleton that binds the config, the boto session, and the CDK stacks.
- Two sample stacks (``alerts_stack`` and ``publisher_stack``), each with a typed exports module that reads its CloudFormation outputs.
- ``cdk-<synth|plan|up|down>-<env>-<stack>`` and ``-all`` mise tasks, generated from the stack enum by ``mise run cdk-gen-tasks``; ``mise run print-cdk-stack-urls`` prints the CloudFormation console link of every stack.
- Unit tests that synthesize each stack without calling AWS, and integration tests (``tests_int/``) that check the deployed stack exports.
- Python tooling: uv, ruff, pytest with coverage, Sphinx docs on Read the Docs, GitHub Actions CI, and Codecov.
- Claude Code skills for the project, including ``pywf-aws-cdk-base`` that explains how the project is organized and how to change it.
- Choose ``MIT``, ``AGPL-3.0-or-later``, or ``LicenseRef-Proprietary``; the post-generation hook writes the matching ``LICENSE.txt``.
- Pick the AWS region every environment deploys to with ``aws_region``.
- After generation, ``.env`` and the ``config/config-*-secret.json5`` files are copied from their examples, and next steps are printed.
- Enter the AWS account id of each environment with ``dev_aws_account_id``, ``tst_aws_account_id`` and ``prd_aws_account_id``; the post-generation hook writes them into ``config/config-<env>-secret.json5``.
