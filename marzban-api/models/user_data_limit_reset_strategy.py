# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UserDataLimitResetStrategy(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    NO_RESET = 'no_reset'
    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'
    YEAR = 'year'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserDataLimitResetStrategy from a JSON string"""
        return cls(json.loads(json_str))


