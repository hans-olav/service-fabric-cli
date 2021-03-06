# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ManagedApplicationIdentity(Model):
    """Describes a managed application identity.

    :param name: The name of the identity.
    :type name: str
    :param principal_id: The identity's PrincipalId.
    :type principal_id: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'principal_id': {'key': 'PrincipalId', 'type': 'str'},
    }

    def __init__(self, name, principal_id=None):
        super(ManagedApplicationIdentity, self).__init__()
        self.name = name
        self.principal_id = principal_id
