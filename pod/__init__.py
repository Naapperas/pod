# pylint: disable=line-too-long
"""Validator package.

The purpose of this package is to provide a set of functions to validate data, using a Zod-like syntax.
"""

__version__ = "0.0.1"
__author__ = "Nuno Pereira"
__email__ = "nunoafonso2002@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2023, Nuno Pereira"

from .base import Pod
from .bool_pod import PodBoolean
from .float_pod import PodFloat
from .int_pod import PodInteger
from .list_pod import PodList
from .number_pod import PodNumber
from .str_pod import PodString
from .union_pod import PodUnion
from .record_pod import PodRecord


def string() -> "PodString":
    """Creates a new Pod that validates that the data is a string.

    Returns:
        PodString: a new validator that validates that the data is a string.
    """
    return PodString()


def number() -> "PodNumber":
    """Creates a new Pod that validates that the data is a number, i.e., an int or a float.

    Returns:
        PodNumber: a new validator that validates that the data is a number.
    """
    return PodNumber()


def integer() -> "PodInteger":
    """Creates a new Pod that validates that the data is an integer.

    Returns:
        PodInteger: a new validator that validates that the data is an integer
    """
    return PodInteger()


def floating_point() -> "PodFloat":
    """Creates a new Pod that validates that the data is a floating point number.

    Returns:
        PodFloat: a new validator that validates that the data is a floating point number.
    """
    return PodFloat()


def boolean() -> "PodBoolean":
    """Creates a new Pod that validates that the data is a boolean.

    Returns:
        PodBoolean: a new validator that validates that the data is a boolean.
    """
    return PodBoolean()


def element_list(element_type: "Pod") -> "PodList":
    """Creates a new Pod that validates that the data is a list of elements of the specified type.

    Args:
        element_type (Pod): the type of the elements of the list.

    Returns:
        PodList: a new validator that validates that the data is
        a list of elements of the specified type.
    """
    return PodList(element_type)


def union(types: list["Pod"]) -> "PodUnion":
    """Creates a new Pod that validates that the data is one of the specified types.

    Args:
        types (list[Pod]): the types of the data to be validated.

    Returns:
        PodUnion: a new validator that validates that the data is one of the specified types.
    """
    return PodUnion(types)


def record(properties: dict[str, "Pod"]) -> "PodRecord":
    """Creates a new Pod that validates that the data is an object with the specified properties.

    Args:
        properties (dict[str, Pod]): the properties of the object to be validated.

    Returns:
        PodObject: a new validator that validates that the data is
        an object with the specified properties.
    """
    return PodRecord(properties)
