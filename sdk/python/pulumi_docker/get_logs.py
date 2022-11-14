# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetLogsResult',
    'AwaitableGetLogsResult',
    'get_logs',
    'get_logs_output',
]

@pulumi.output_type
class GetLogsResult:
    """
    A collection of values returned by getLogs.
    """
    def __init__(__self__, details=None, discard_headers=None, follow=None, id=None, logs_list_string_enabled=None, logs_list_strings=None, name=None, show_stderr=None, show_stdout=None, since=None, tail=None, timestamps=None, until=None):
        if details and not isinstance(details, bool):
            raise TypeError("Expected argument 'details' to be a bool")
        pulumi.set(__self__, "details", details)
        if discard_headers and not isinstance(discard_headers, bool):
            raise TypeError("Expected argument 'discard_headers' to be a bool")
        pulumi.set(__self__, "discard_headers", discard_headers)
        if follow and not isinstance(follow, bool):
            raise TypeError("Expected argument 'follow' to be a bool")
        pulumi.set(__self__, "follow", follow)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if logs_list_string_enabled and not isinstance(logs_list_string_enabled, bool):
            raise TypeError("Expected argument 'logs_list_string_enabled' to be a bool")
        pulumi.set(__self__, "logs_list_string_enabled", logs_list_string_enabled)
        if logs_list_strings and not isinstance(logs_list_strings, list):
            raise TypeError("Expected argument 'logs_list_strings' to be a list")
        pulumi.set(__self__, "logs_list_strings", logs_list_strings)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if show_stderr and not isinstance(show_stderr, bool):
            raise TypeError("Expected argument 'show_stderr' to be a bool")
        pulumi.set(__self__, "show_stderr", show_stderr)
        if show_stdout and not isinstance(show_stdout, bool):
            raise TypeError("Expected argument 'show_stdout' to be a bool")
        pulumi.set(__self__, "show_stdout", show_stdout)
        if since and not isinstance(since, str):
            raise TypeError("Expected argument 'since' to be a str")
        pulumi.set(__self__, "since", since)
        if tail and not isinstance(tail, str):
            raise TypeError("Expected argument 'tail' to be a str")
        pulumi.set(__self__, "tail", tail)
        if timestamps and not isinstance(timestamps, bool):
            raise TypeError("Expected argument 'timestamps' to be a bool")
        pulumi.set(__self__, "timestamps", timestamps)
        if until and not isinstance(until, str):
            raise TypeError("Expected argument 'until' to be a str")
        pulumi.set(__self__, "until", until)

    @property
    @pulumi.getter
    def details(self) -> Optional[bool]:
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="discardHeaders")
    def discard_headers(self) -> Optional[bool]:
        """
        Discard headers that docker appends to each log entry
        """
        return pulumi.get(self, "discard_headers")

    @property
    @pulumi.getter
    def follow(self) -> Optional[bool]:
        return pulumi.get(self, "follow")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="logsListStringEnabled")
    def logs_list_string_enabled(self) -> Optional[bool]:
        """
        If true populate computed value `logs_list_string`
        """
        return pulumi.get(self, "logs_list_string_enabled")

    @property
    @pulumi.getter(name="logsListStrings")
    def logs_list_strings(self) -> Sequence[str]:
        """
        List of container logs, each element is a line.
        """
        return pulumi.get(self, "logs_list_strings")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the Docker Container
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="showStderr")
    def show_stderr(self) -> Optional[bool]:
        return pulumi.get(self, "show_stderr")

    @property
    @pulumi.getter(name="showStdout")
    def show_stdout(self) -> Optional[bool]:
        return pulumi.get(self, "show_stdout")

    @property
    @pulumi.getter
    def since(self) -> Optional[str]:
        return pulumi.get(self, "since")

    @property
    @pulumi.getter
    def tail(self) -> Optional[str]:
        return pulumi.get(self, "tail")

    @property
    @pulumi.getter
    def timestamps(self) -> Optional[bool]:
        return pulumi.get(self, "timestamps")

    @property
    @pulumi.getter
    def until(self) -> Optional[str]:
        return pulumi.get(self, "until")


class AwaitableGetLogsResult(GetLogsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLogsResult(
            details=self.details,
            discard_headers=self.discard_headers,
            follow=self.follow,
            id=self.id,
            logs_list_string_enabled=self.logs_list_string_enabled,
            logs_list_strings=self.logs_list_strings,
            name=self.name,
            show_stderr=self.show_stderr,
            show_stdout=self.show_stdout,
            since=self.since,
            tail=self.tail,
            timestamps=self.timestamps,
            until=self.until)


def get_logs(details: Optional[bool] = None,
             discard_headers: Optional[bool] = None,
             follow: Optional[bool] = None,
             logs_list_string_enabled: Optional[bool] = None,
             name: Optional[str] = None,
             show_stderr: Optional[bool] = None,
             show_stdout: Optional[bool] = None,
             since: Optional[str] = None,
             tail: Optional[str] = None,
             timestamps: Optional[bool] = None,
             until: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLogsResult:
    """
    `get_logs` provides logs from specific container


    :param bool discard_headers: Discard headers that docker appends to each log entry
    :param bool logs_list_string_enabled: If true populate computed value `logs_list_string`
    :param str name: The name of the Docker Container
    """
    __args__ = dict()
    __args__['details'] = details
    __args__['discardHeaders'] = discard_headers
    __args__['follow'] = follow
    __args__['logsListStringEnabled'] = logs_list_string_enabled
    __args__['name'] = name
    __args__['showStderr'] = show_stderr
    __args__['showStdout'] = show_stdout
    __args__['since'] = since
    __args__['tail'] = tail
    __args__['timestamps'] = timestamps
    __args__['until'] = until
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('docker:index/getLogs:getLogs', __args__, opts=opts, typ=GetLogsResult).value

    return AwaitableGetLogsResult(
        details=__ret__.details,
        discard_headers=__ret__.discard_headers,
        follow=__ret__.follow,
        id=__ret__.id,
        logs_list_string_enabled=__ret__.logs_list_string_enabled,
        logs_list_strings=__ret__.logs_list_strings,
        name=__ret__.name,
        show_stderr=__ret__.show_stderr,
        show_stdout=__ret__.show_stdout,
        since=__ret__.since,
        tail=__ret__.tail,
        timestamps=__ret__.timestamps,
        until=__ret__.until)


@_utilities.lift_output_func(get_logs)
def get_logs_output(details: Optional[pulumi.Input[Optional[bool]]] = None,
                    discard_headers: Optional[pulumi.Input[Optional[bool]]] = None,
                    follow: Optional[pulumi.Input[Optional[bool]]] = None,
                    logs_list_string_enabled: Optional[pulumi.Input[Optional[bool]]] = None,
                    name: Optional[pulumi.Input[str]] = None,
                    show_stderr: Optional[pulumi.Input[Optional[bool]]] = None,
                    show_stdout: Optional[pulumi.Input[Optional[bool]]] = None,
                    since: Optional[pulumi.Input[Optional[str]]] = None,
                    tail: Optional[pulumi.Input[Optional[str]]] = None,
                    timestamps: Optional[pulumi.Input[Optional[bool]]] = None,
                    until: Optional[pulumi.Input[Optional[str]]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLogsResult]:
    """
    `get_logs` provides logs from specific container


    :param bool discard_headers: Discard headers that docker appends to each log entry
    :param bool logs_list_string_enabled: If true populate computed value `logs_list_string`
    :param str name: The name of the Docker Container
    """
    ...
