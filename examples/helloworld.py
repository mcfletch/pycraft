# We need to expose our function to pycraft,
# the function to do that is stored in a python module (file)
# that is found using the name `pycraft.expose`
# and is named `expose` in that module.
# We here ask python to look for where the module is,
# load it, and make the name `expose` from the module
# available here to use that function.
from pycraft.expose import expose


# def is short for "define function" You'll find that other
# programming languages will use various short-forms of this,
# or sometimes "procedures". The basic idea of a function is
# that you have some common bit of code that you want to use
# over and over again. The parens `()` to the right of the
# function name `hello_world` define the set of `parameters`
# or `arguments` that will be passed into the function.
# Here the function is so simple that it doesn't take any
# arguments.
#
# @expose is a "decorator", think of it like saying
# we want lots of functions to do something similar, so
# we will make something that can change the functions to
# do that thing.
# Here the decorator "exposes the function in the default chat namespace"
#
# async isn't actually necessary here, but almost everything
# we'll be doing wants to be asynchronous. What does that mean?
# For our purposes it means "able to wait for things to happen"
# So when we talk to the server, we'll say `await call()`
# and the function would stop and wait for the response before
# it carries on processing.
@expose()
async def hello_world():
    # return allows us to give the caller of our function a
    # result back. The result might be a simple string, and integer,
    # or a complex object we've built from the server.
    return "Hello World!"
