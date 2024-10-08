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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.template_component import TemplateComponent
from typing import Optional, Set
from typing_extensions import Self

class TemplatePost(BaseModel):
    """
    TemplatePost
    """ # noqa: E501
    id_project: StrictStr = Field(description="Id of current project")
    name: StrictStr = Field(description="Name of template")
    category: StrictStr = Field(description="Category of template")
    allow_category_change: StrictBool = Field(description="Allow category change of template")
    language: StrictStr = Field(description="Language of template")
    components: List[TemplateComponent] = Field(description="Components of template")
    __properties: ClassVar[List[str]] = ["id_project", "name", "category", "allow_category_change", "language", "components"]

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
        """Create an instance of TemplatePost from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in components (list)
        _items = []
        if self.components:
            for _item in self.components:
                if _item:
                    _items.append(_item.to_dict())
            _dict['components'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TemplatePost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id_project": obj.get("id_project"),
            "name": obj.get("name"),
            "category": obj.get("category"),
            "allow_category_change": obj.get("allow_category_change"),
            "language": obj.get("language"),
            "components": [TemplateComponent.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None
        })
        return _obj


