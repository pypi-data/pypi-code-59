import base64
from http.client import RemoteDisconnected
import json
import logging
import os
import subprocess
import threading
import time
from typing import Any, Dict, List, Tuple

import click
from ray.autoscaler.node_provider import get_node_provider, NODE_PROVIDERS, NodeProvider
from ray.autoscaler.tags import NODE_TYPE_HEAD, NODE_TYPE_WORKER, TAG_RAY_NODE_TYPE
from ray.autoscaler.util import validate_config
import yaml

from anyscale.util import send_json_request

logger = logging.getLogger(__name__)

try:
    import requests
except ImportError:
    logger.exception(
        "Couldn't import `requests` library. Try installing it with `pip install requests`."
    )

ClusterName = str
ProviderConfig = Dict[str, str]
ClusterConfig = Dict[str, Any]
Request = Dict[str, Any]
Response = Dict[str, Any]


class CloudGatewayRunner:
    """Initializes and runs the cloud gateway.

    Args:
        provider_path (str): the path to the provider config.
        anyscale_address (str): the address to the anyscale end point.
    Raises:
        ValueError: if the provider_path file includes keys different from "provider".

    """

    def __init__(self, provider_path: str, anyscale_address: str) -> None:
        with open(provider_path) as f:
            provider_config = yaml.safe_load(f)
            self.provider_config = provider_config["provider"]
            if len(provider_config.keys()) > 1:
                raise ValueError(
                    "Expecting a provider config that includes only provider configurations."
                )
            if self.provider_config["type"] == "local":
                self.available_node_ips = self.provider_config["worker_ips"]
                if self.provider_config["head_ip"]:
                    logger.warning(
                        "There is no difference between head_ip and worker_ips when running the cloudgateway with a provider of type local."
                    )
                    self.available_node_ips.append(self.provider_config["head_ip"])
                self.used_node_ips: List[str] = []
        self.anyscale_address = anyscale_address
        self.cached_node_providers: Dict[ClusterName, NodeProvider] = {}

    def _get_bootstrapped_config(self, mixed_config: ClusterConfig) -> Any:
        """Receives the cluster yaml and bootsrapped configs."""
        try:
            importer = NODE_PROVIDERS.get(mixed_config["provider"]["type"])
        except NotImplementedError:
            raise NotImplementedError(
                "Unsupported provider {}".format(mixed_config["provider"]["type"])
            )
        bootstrap_config, _ = importer()
        if bootstrap_config:
            bootstrapped_config = bootstrap_config(mixed_config)
        else:
            bootstrapped_config = mixed_config
        return bootstrapped_config

    def _get_updated_local_provider_config(
        self, provider_config: ProviderConfig
    ) -> ProviderConfig:
        """This function manages which ips each local cluster gets."""
        pass

    def _get_cluster_name_and_provider(
        self, request: Request
    ) -> Tuple[ClusterName, NodeProvider, ProviderConfig]:
        """Receives the request and returns the cluster name, node provider and provider config."""
        # cluster_name is unique per node_provider
        cluster_name = request["cluster_name"]
        # TODO(ameer): next PR will modify this to account for resource allocation
        provider_config = self.provider_config
        if cluster_name in self.cached_node_providers:
            node_provider = self.cached_node_providers[cluster_name]
        else:
            node_provider = get_node_provider(provider_config, cluster_name)
            self.cached_node_providers[cluster_name] = node_provider
        return cluster_name, node_provider, provider_config

    def _process_request(
        self,
        request: Request,
        cluster_name: ClusterName,
        node_provider: NodeProvider,
        provider_config: ProviderConfig,
    ) -> Response:
        """Receives the request and processes it."""
        # TODO(ameer): make it multithreaded to support simultaneous execution
        provider_request_types = [
            "non_terminated_nodes",
            "is_running",
            "is_terminated",
            "node_tags",
            "external_ip",
            "internal_ip",
            "create_node",
            "set_node_tags",
            "terminate_node",
            "terminate_nodes",
            "cleanup",
        ]
        cmd_runner_request_types = [
            "cmd_runner.run",
            "cmd_runner.run_rsync_up",
            "cmd_runner.run_rsync_down",
            "cmd_runner.remote_shell_command_str",
        ]
        if request["type"] in provider_request_types:
            response = self._handle_node_provider_requests(
                request, cluster_name, node_provider, provider_config
            )
        elif request["type"] in cmd_runner_request_types:
            response = self._handle_cmd_runner_request(request, node_provider)
        else:
            logger.error(
                "The cloud gateway does not support request of type: " + request["type"]
            )
            response = None
        response_message = {"data": response, "request_id": request["request_id"]}
        return response_message

    def _handle_cmd_runner_request(
        self, request: Request, node_provider: NodeProvider
    ) -> Any:
        """Handles command runner requests."""
        response: Any = None
        if request["type"] == "cmd_runner.run":
            cmd_runner_kwargs, cmd, run_args, run_kwargs = request["args"]
            cmd = self._temporary_aws_credentials_if_necessary(cmd)
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            try:
                cmd_runner.run(cmd, *run_args, **run_kwargs)
                response = None
            except Exception as e:
                if isinstance(e, click.ClickException):
                    response = {
                        "exception_type": "click.ClickException",
                        "error_str": str(e),
                    }
                elif isinstance(e, subprocess.CalledProcessError):
                    response = {
                        "exception_type": "subprocess.CalledProcessError",
                        "returncode": e.returncode,
                        "cmd": e.cmd,
                    }
                else:
                    response = {"exception_type": "Exception", "error_str": str(e)}
        elif request["type"] == "cmd_runner.run_rsync_up":
            cmd_runner_kwargs, source, target, content, mode = request["args"]
            try:
                # Store source file on the gateway node.
                with open(os.path.expanduser(source), "wb") as f:
                    f.write(base64.b64decode(content))
            except PermissionError:
                logger.warning("File already exists.")
            os.chmod(source, mode)
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            cmd_runner.run_rsync_up(source, target)
            response = None
        elif request["type"] == "cmd_runner.run_rsync_down":
            cmd_runner_kwargs, source, target = request["args"]
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            # rsync the source file to the the gateway node with file name <target>.
            cmd_runner.run_rsync_down(source, target)
            if not os.path.isfile(target):
                raise ValueError(
                    "The cloudgateway supports downloading a single file only."
                )
            mode = os.stat(target).st_mode & 0o777
            try:
                with open(target, "rb") as f:
                    # Decode makes it json dumpable.
                    content = base64.b64encode(f.read()).decode()
                    response = {"content": content, "mode": mode}
            except FileNotFoundError:
                response = {"content": None, "mode": None}
        elif request["type"] == "cmd_runner.remote_shell_command_str":
            cmd_runner_kwargs = request["args"]
            cmd_runner = node_provider.get_command_runner(
                **cmd_runner_kwargs, process_runner=subprocess
            )
            response = cmd_runner.remote_shell_command_str()
        else:
            raise NotImplementedError
        return response

    def _handle_node_provider_requests(
        self,
        request: Request,
        cluster_name: ClusterName,
        node_provider: NodeProvider,
        provider_config: ProviderConfig,
    ) -> Any:
        """Handles node provider requests."""
        response: Any = None
        if request["type"] == "create_node":
            node_config, tags, count, cluster_config = request["args"]
            if tags[TAG_RAY_NODE_TYPE] == NODE_TYPE_HEAD:
                node_type = "head_node"
            elif tags[TAG_RAY_NODE_TYPE] == NODE_TYPE_WORKER:
                node_type = "worker_nodes"
            else:
                raise NotImplementedError(
                    "The cloud gateway does not support node type: "
                    + tags[TAG_RAY_NODE_TYPE]
                )
            mixed_config = cluster_config
            mixed_config["provider"] = provider_config
            autoscaling = not (
                mixed_config["initial_workers"] == mixed_config["min_workers"]
                and mixed_config["initial_workers"] == mixed_config["max_workers"]
            )
            if mixed_config["provider"]["type"] == "local" and autoscaling:
                logger.error(
                    "The cloud gateway does not support autoscaling in local mode."
                    + " The gateway will allocate max_workers to cluster: "
                    + cluster_name
                )
            mixed_config["cluster_name"] = cluster_name
            bootstrapped_config = self._get_bootstrapped_config(mixed_config)
            response = getattr(node_provider, request["type"])(
                bootstrapped_config[node_type], tags, count
            )
        else:
            response = getattr(node_provider, request["type"])(*request["args"])
        return response

    def _temporary_aws_credentials_if_necessary(self, cmd: str) -> str:
        """The temporary aws credentials if necessary for temporary access to S3."""
        new_cmd = cmd
        # TODO(ameer): This is really ugly
        if "s3:s3.amazonaws.com" in cmd and "RESTIC_PASSWORD=program_the_cloud" in cmd:
            try:
                resp = send_json_request("/api/v2/users/temporary_aws_credentials", {})
                aws_credentials_vars = " ".join(
                    [key + "=" + resp["result"][key] for key in resp["result"]]
                )
            except Exception as e:
                # The snapshot may not exist.
                raise click.ClickException(e)  # type: ignore

            new_cmd = cmd.replace(
                "RESTIC_PASSWORD=program_the_cloud",
                aws_credentials_vars + " RESTIC_PASSWORD=program_the_cloud",
            )

        return new_cmd

    def gateway_run_forever(self) -> None:
        """Long polls anyscale server."""
        # TODO(ameer): make this run in the background,
        # need to fix the autoscaler cleanup function.
        self._run()

    def _run(self) -> None:
        response_message = {"data": "first_message", "request_id": "0"}
        while 1:
            try:
                request = send_json_request(
                    self.anyscale_address,
                    {"response": json.dumps(response_message)},
                    method="GET",
                )
            except Exception:
                logger.exception("Could not connect to Anyscale server. Retrying...")
                response_message = {"data": "first_message", "request_id": "0"}
                time.sleep(10)
                continue
            logger.info("Received request: " + str(request["result"]["type"]))
            (
                cluster_name,
                node_provider,
                provider_config,
            ) = self._get_cluster_name_and_provider(request["result"])
            response_message = self._process_request(
                request["result"], cluster_name, node_provider, provider_config
            )
