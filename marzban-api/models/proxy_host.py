# coding: utf-8

"""
    MarzbanAPI

    Unified GUI Censorship Resistant Solution Powered by Xray

    The version of the OpenAPI document: 0.4.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from marzban-api.models.proxy_host_alpn import ProxyHostALPN
from marzban-api.models.proxy_host_fingerprint import ProxyHostFingerprint
from marzban-api.models.proxy_host_security import ProxyHostSecurity
from typing import Optional, Set
from typing_extensions import Self

class ProxyHost(BaseModel):
    """
    ProxyHost
    """ # noqa: E501
    remark: StrictStr
    address: StrictStr
    port: Optional[StrictInt] = None
    sni: Optional[StrictStr] = None
    host: Optional[StrictStr] = None
    security: Optional[ProxyHostSecurity] = None
    alpn: Optional[ProxyHostALPN] = None
    fingerprint: Optional[ProxyHostFingerprint] = None
    allowinsecure: Optional[StrictBool] = None
    is_disabled: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["remark", "address", "port", "sni", "host", "security", "alpn", "fingerprint", "allowinsecure", "is_disabled"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ProxyHost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if sni (nullable) is None
        # and model_fields_set contains the field
        if self.sni is None and "sni" in self.model_fields_set:
            _dict['sni'] = None

        # set to None if host (nullable) is None
        # and model_fields_set contains the field
        if self.host is None and "host" in self.model_fields_set:
            _dict['host'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProxyHost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "remark": obj.get("remark"),
            "address": obj.get("address"),
            "port": obj.get("port"),
            "sni": obj.get("sni"),
            "host": obj.get("host"),
            "security": obj.get("security"),
            "alpn": obj.get("alpn"),
            "fingerprint": obj.get("fingerprint"),
            "allowinsecure": obj.get("allowinsecure"),
            "is_disabled": obj.get("is_disabled")
        })
        return _obj


