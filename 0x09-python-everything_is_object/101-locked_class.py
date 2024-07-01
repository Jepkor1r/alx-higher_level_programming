#!/usr/bin/python3
"""
    LockedClass: class with no class or object attribute,
    that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name
    __slot__: restricts creation of dynamic attributes,
    leading to a more efficient and predictable classes
"""


class LockedClass:
    """
        LockedClass: class with no class or object attribute.
        It prevents the user from dynamically creating new instance attributes,
        except if the new instance attribute is called first_name
        __slot__: restricts creation of dynamic attributes,
        leading to a more efficient and predictable classes
        __init__: self initializiation
    """
    __slots__ = ['first_name']

    def __init__(self, first_name):
        self.first_name = first_name
