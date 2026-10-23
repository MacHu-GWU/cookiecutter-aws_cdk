.. _release_history:

Release and Version History
==============================================================================


Backlog (TODO)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.0.0 (2026-10-23)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seed repo changes: `1.0.0 (2026-10-23) <https://github.com/MacHu-GWU/cookiecutter_aws_cdk_demo-project/blob/1.0.0/release-history-seed-repo.rst#100-2026-10-23>`__

**Features and Improvements**

- The template and its seed repo now share one version number, so a template version also names the seed state it was generated from. The version jumps from ``0.1.1`` to ``1.0.0`` for this reason only: generating a project works exactly as with ``0.1.1``, and no variable changed
- Every release entry in this file now starts with a link to the seed repo's own changelog (``release-history-seed-repo.rst``) at the seed's tag of the same version, which lists what newly generated projects get

**Minor Improvements**

- A published version is never overwritten: ``mise run publish-template`` creates the tag and the GitHub release in one step, refuses a version that already has a tag, and links the release to its changelog entry
- New ``mise run publish-presets`` regenerates the ``preset/*`` branches from the pushed ``main``; ``publish-template`` runs it last, and it can be rerun alone, for example after changing only ``presets/*.json``
- New ``mise run check-release``: before anything is pushed, checks the version is the same in the seed and in this repo, the template is current, the seed is pushed and tagged, and the changelog entry starts with the seed link
- New ``mise run check-version``, run by ``mise run sync``: the seed version is valid, documented in the seed's changelog, never recorded in the template's own ``release-history.rst``, and every link of the generated ``pywf-aws-cdk-base`` skill points at the seed's tag of that version
- New ``mise run e2e``: ``sync`` followed by ``try-template``, one command from the seed to a tested generated project
- The seed's tag of the same version records which seed commit a template version was built from; changelog entries no longer carry a ``Built from seed`` commit

**Miscellaneous**

- ``mise run sync`` copies the seed version into this repo's ``pyproject.toml`` and ``uv.lock``; the version is never edited here
- New ``cctpl-changelog-cn`` skill writes this file, replacing ``py-changelog``; the cctpl skills describe the shared version, the seed-only files, and the new release order


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
