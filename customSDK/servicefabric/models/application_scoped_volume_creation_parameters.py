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


class ApplicationScopedVolumeCreationParameters(Model):
    """Describes parameters for creating application-scoped volumes.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are:
    ApplicationScopedVolumeCreationParametersServiceFabricVolumeDisk

    :param description: User readable description of the volume.
    :type description: str
    :param kind: Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'ServiceFabricVolumeDisk': 'ApplicationScopedVolumeCreationParametersServiceFabricVolumeDisk'}
    }

    def __init__(self, description=None):
        super(ApplicationScopedVolumeCreationParameters, self).__init__()
        self.description = description
        self.kind = None
