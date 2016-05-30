# A module's \_\_name\_\_

For every python module there will be a few variables/attributes available. One of them is `__name__`. The value of `__name__` will change depending on how we execute our module. There are two options:
* Execute the module directly (`python my_module.py`). In this case, `__name__` will have the value `__main__`. **Always**.
* Importing the module from other packge (`import my_module`). In this case the value will be the name of the module

We can execute code inside a python module in 2 different ways:
* By invoking the module directly: `python my_module.py`, or
* by importing it from other module

We can see this with two simple examples:

```python
python example-3-__name__/my_module.py
```

In this case the value will be `__main__`.

```python
python example-3-__name__/main.py
```

In this case the value will be `my_module`.
