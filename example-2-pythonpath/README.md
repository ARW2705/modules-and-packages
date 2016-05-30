# PYTHONPATH

Python's Path is similar to Bash's Path. It provides an array or list of places where Python can search when it needs to import a module. `PYTHONPATH` is an environment variable that can be used to augment Python path's at the moment of execute our programs.

## Example 1
Try running the `example_1.py` module with and without the `PYTHONPATH` variable.

```python
python example-2-pythonpath/example_1.py
```
In the first list of the array of paths you'll see something similar to `.../python-modules-and-packages-practice/example-2-pythonpath'`. That's because **python adds the location of the executed script automatically to the Python Path**. Now try running it specifying the `PYTHONPATH` variable:

```python
PYTHONPATH=. python example-2-pythonpath/example_1.py
```

In this example, the dot represents the current directory. That means that you'll be able to see the root directory of this repo (`/python-modules-and-packages-practice`) in the Path.

## Example 2

The second example tries to import a module in a strange location. We'll try to run it and we'll get an error:

```python
python example-2-pythonpath/example_2.py
```

We get the following error:

```
Traceback (most recent call last):
  File "example-2-pythonpath/example_2.py", line 1, in <module>
    import a_weird_module
ImportError: No module named a_weird_module
```

That's expected, because when Python searches for `a_weird_module` through it's list of location in `PYTHONPATH`, it can't find it. So, let's add the location to the PYTHONPATH to make this work:


```python
PYTHONPATH=./example-2-pythonpath/a_weird_location python example-2-pythonpath/example_2.py
```

Now you'll see it working. We've manually added a new location where Python can search for modules.

## Example 3

We can also modify the `PYTHONPATH` from within the Python script, using the `sys.path` variable. See `example_3.py` and try running it.
