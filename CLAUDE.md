# CLAUDE.md

This is the **tpl repo** of a cookiecutter template for multi-environment AWS CDK projects in Python. The template is never edited directly: it is generated from a runnable **seed repo** (path: `CCTPL_SEED_DIR` in `mise.toml`) and published from here.

All maintenance rules live in the `cctpl-*-cn` skill family under `.claude/skills/`. Start with `cctpl-base-cn/SKILL.md`; it is the single source of truth and says which invoker fits which job:

| Job | Skill |
| :--- | :--- |
| Change the template (content or mechanism) | `/cctpl-change-cn` |
| Add, change, or remove a cookiecutter variable | `/cctpl-add-param-cn` |
| Regenerate the template from the seed and run all checks | `/cctpl-sync-cn` |
| Try a generated project locally | `/cctpl-try-cn` |
| Prepare a release (user only) | `/cctpl-release-cn` |
| Verify the published template (user only) | `/cctpl-verify-cn` |
| Copy this skill family to another tpl / seed repo pair, once (user only) | `/cctpl-fork-cn` |

Two rules that hold even before a skill is loaded (details: `cctpl-base-cn/references/04-safety-rules.md`):

- Never run git write operations or `mise run publish-template`; print the commands for the user instead.
- Never edit `cookiecutter.json`, `{{ cookiecutter.package_name }}-project/` or `README.rst` by hand; change the seed (or the parameterization) and run `mise run sync`.

## Current Status

Open items for this pair (keep this short; delete items when done):

- This pair was forked from `cookiecutter-pywf_open_source` by copy and string replacement, then adapted. Nothing is published yet: the GitHub repo `MacHu-GWU/cookiecutter-aws_cdk` does not exist and this checkout has no `origin` remote. The user creates both before the first `mise run publish-template`.
- 0.1.1 is the first release: run `/cctpl-release-cn` (writes its changelog entry and seed commit), publish, then `/cctpl-verify-cn`.
