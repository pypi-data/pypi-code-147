#!/usr/bin/env python
# -*- coding:utf-8 -*-
from functools import wraps
from typing import Callable, Type

from ._hook import _get_chain, _run_hook_func


def capture(exception: Type[Exception] = Exception, post_hook: Callable = None):
    """
    Catch exceptions to decorated functions, including exceptions generated by other decorators.

    callback functions can and only support communication via the chain keyword parameter. example: callback() is ok,
    callback(chain=None) is ok, callback(chain=None, other=None) is ok(other arg will not be assigned), callback(other, chain=None) will happend exception

    :param post_hook: while callback function when happen exception
    :param exception: The base type exception to the exception that needs to be caught. After capture,
                    the exception will be "eaten" directly, and exception outside this range will be thrown.
    :return:
    """

    def _inner(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            chain, func_new_kwargs = _get_chain(func, args, kwargs)
            try:
                return func(*args, *kwargs)
            except BaseException as e:
                if issubclass(type(e), exception):
                    raise
            finally:
                _run_hook_func([post_hook], chain, func_new_kwargs)

        return _wrapper

    return _inner


__all__ = [capture]
