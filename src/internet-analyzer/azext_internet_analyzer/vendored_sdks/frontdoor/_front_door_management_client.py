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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import FrontDoorManagementClientConfiguration
from .operations import FrontDoorManagementClientOperationsMixin
from .operations import NetworkExperimentProfilesOperations
from .operations import PreconfiguredEndpointsOperations
from .operations import ExperimentsOperations
from .operations import ReportsOperations
from .operations import FrontDoorsOperations
from .operations import FrontendEndpointsOperations
from .operations import EndpointsOperations
from .operations import PoliciesOperations
from .operations import ManagedRuleSetsOperations
from . import models


class FrontDoorManagementClient(FrontDoorManagementClientOperationsMixin, SDKClient):
    """FrontDoor Client

    :ivar config: Configuration for client.
    :vartype config: FrontDoorManagementClientConfiguration

    :ivar network_experiment_profiles: NetworkExperimentProfiles operations
    :vartype network_experiment_profiles: azure.mgmt.frontdoor.operations.NetworkExperimentProfilesOperations
    :ivar preconfigured_endpoints: PreconfiguredEndpoints operations
    :vartype preconfigured_endpoints: azure.mgmt.frontdoor.operations.PreconfiguredEndpointsOperations
    :ivar experiments: Experiments operations
    :vartype experiments: azure.mgmt.frontdoor.operations.ExperimentsOperations
    :ivar reports: Reports operations
    :vartype reports: azure.mgmt.frontdoor.operations.ReportsOperations
    :ivar front_doors: FrontDoors operations
    :vartype front_doors: azure.mgmt.frontdoor.operations.FrontDoorsOperations
    :ivar frontend_endpoints: FrontendEndpoints operations
    :vartype frontend_endpoints: azure.mgmt.frontdoor.operations.FrontendEndpointsOperations
    :ivar endpoints: Endpoints operations
    :vartype endpoints: azure.mgmt.frontdoor.operations.EndpointsOperations
    :ivar policies: Policies operations
    :vartype policies: azure.mgmt.frontdoor.operations.PoliciesOperations
    :ivar managed_rule_sets: ManagedRuleSets operations
    :vartype managed_rule_sets: azure.mgmt.frontdoor.operations.ManagedRuleSetsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription credentials which uniquely
     identify the Microsoft Azure subscription. The subscription ID forms part
     of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = FrontDoorManagementClientConfiguration(credentials, subscription_id, base_url)
        super(FrontDoorManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.network_experiment_profiles = NetworkExperimentProfilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.preconfigured_endpoints = PreconfiguredEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.experiments = ExperimentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.reports = ReportsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.front_doors = FrontDoorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.frontend_endpoints = FrontendEndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.endpoints = EndpointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.policies = PoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.managed_rule_sets = ManagedRuleSetsOperations(
            self._client, self.config, self._serialize, self._deserialize)
