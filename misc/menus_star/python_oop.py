import marimo

__generated_with = "0.13.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""## 1. Functional Programming""")
    return


app._unparsable_cell(
    r"""
    def 
    """,
    name="_"
)


@app.cell
def _():
    def foo(x):
        _x = x
        def bar(y):
            return _x + y
        return {'x': _x, 'shift': bar}

    obj0 = foo(10)
    obj1 = foo(20)
    print(obj0,obj1)
    print('Translate',obj0['x'],obj0['shift'](20))
    return


@app.cell
def _():
    class Foo:
        def __init__(self,x):
            _private = 123
            self._x = x
            self.quz = lambda y: self._x * y + _private

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self,xx):
            self._x = xx

        def bar(self,y):
            return self._x + y

        def __repr__(self):
            return f'x: {self._x}'
        
        def __str__(self):
            return f'print x: {self._x}'


    objoop0 = Foo(10)
    objoop0.x = 35
    print(objoop0)
    objoop0.x,objoop0.bar(20),objoop0.quz(1.5)
    return (Foo,)


@app.cell
def _(Foo):
    objoop1 = Foo(20)
    objoop1.bar(20),objoop1.quz(1.5)
    objoop1
    return


@app.cell
def _(mo):
    mo.md(r"""## Decorator and closure""")
    return


app._unparsable_cell(
    r"""
    # Decorator and Closure
    def baz(fn):
        def wrap(a,b):
            return fn(a,b)
        return wrap

    @baz
    def sum(x,y):
        return x + y

    def 
    print(sum(1,2))
    """,
    name="_"
)


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
