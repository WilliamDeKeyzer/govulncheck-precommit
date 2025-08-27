# Govulncheck pre-commit hook

Enable this to run govulncheck as a pre-commit hook.

You do this by adding the following hook to your `.pre-commit-config.yaml` file in your repository.

```
 - repo: https://github.com/WilliamDeKeyzer/govulncheck-precommit
   hooks:
      - id: govulncheck
        rev: xxx
        always_run: true
```
