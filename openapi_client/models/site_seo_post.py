# coding: utf-8

"""
    API MIAI

    API for integration with MIAI To get started, you need a token where you can get it by do a post request to 'Get account by email and password' and use the token in the header (Authorization: Bearer token) to access the other endpoints 

    The version of the OpenAPI document: 1.0.31
    Contact: oscarsilva@mios.pt
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class SiteSeoPost(BaseModel):
    """
    SiteSeoPost
    """ # noqa: E501
    id_product: StrictStr = Field(description="Id of product")
    base_64_url: StrictStr = Field(description="Base 64 url of product")
    performance: StrictInt = Field(description="Performance of product")
    accessibility: StrictInt = Field(description="Accessibility of product")
    best_practices: StrictInt = Field(description="Best practices of product")
    seo: StrictInt = Field(description="Seo of product")
    html_analytics: StrictStr = Field(description="Html analytics of product")
    __properties: ClassVar[List[str]] = ["id_product", "base_64_url", "performance", "accessibility", "best_practices", "seo", "html_analytics"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SiteSeoPost from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SiteSeoPost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id_product": obj.get("id_product"),
            "base_64_url": obj.get("base_64_url"),
            "performance": obj.get("performance"),
            "accessibility": obj.get("accessibility"),
            "best_practices": obj.get("best_practices"),
            "seo": obj.get("seo"),
            "html_analytics": obj.get("html_analytics")
        })
        return _obj


