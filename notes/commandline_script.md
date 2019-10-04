## Make a CLI like interface

### Add the following to setup.py

```python
entry_points = {
    "console_scripts": ['hephaestus = hephaestus.main:main_routine()']
}
```

## Full steps: https://gehrcke.de/2014/02/distributing-a-python-command-line-application/