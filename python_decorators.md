decorators are shorthand for calling a functions wrapper on a functions
it can also do operations on classes

they're good for a couple things

1. refactoring out repetitive code
2. logging functions
3. memoization (caching results)
4. metrics collection (such as timing)

basically doing stuff with info before it gets to the funct


@log
def x(): pass

is shorthand for x = log(x)

the decorator must return a function
