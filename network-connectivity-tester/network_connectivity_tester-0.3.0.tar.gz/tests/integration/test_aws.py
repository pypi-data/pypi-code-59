from os import path as osp
from os import environ
import os
from pprint import pformat
import boto3
from terraform_ci import terraform_apply, setup_environment
from .conftest import AWS_TEST_ACCOUNT
from network_connectivity_tester.orchestrator import connectivity_tester

setup_environment()


def test_aws():
    # make sure tests run under our test account
    assert boto3.client("sts").get_caller_identity().get("Account") == AWS_TEST_ACCOUNT

    region = "us-east-1"
    whl = [f for f in os.listdir("dist/") if f.endswith(".whl")][0]
    whl = osp.join(os.getcwd(), "dist", whl)

    with connectivity_tester(region=region) as connectivity_test_object:
        environ["TF_VAR_region"] = region
        environ["TF_VAR_install_whl"] = whl
        environ["TF_VAR_registration_queue"] = connectivity_test_object.queue_name

        with terraform_apply(
            "tests/integration/test_data/aws_vpc_two_nodes", json_output=True
        ) as tf_node_out:
            # test connections
            instances = tf_node_out["nodes"]["value"]
            assert connectivity_test_object.wait_for_registrations(instances=instances)

            # for instance in instances:
            test_url = "https://www.google.com/"
            for instance in instances:
                assert connectivity_test_object.test_url(
                    instance=instance, url=test_url
                ), "Unable to connect to %s" % pformat(test_url, indent=4)

            for instance in instances:
                for destination in instances:
                    assert connectivity_test_object.test_ping_internal(
                        source=instance, destination=destination
                    ), "Unable to PING %s from %s" % (destination, instance)

            assert connectivity_test_object.test_tcp(
                source="node1", destination="node2", port=8888
            ), "Unable to Connect node2:8888 from node1"
