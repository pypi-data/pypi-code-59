import asyncio
from unittest import mock
from distutils.util import strtobool
from os import environ
import uuid

import dask
import pytest
from dask.distributed import Client

import coiled

from .conftest import PASSWORD, ACCOUNT, CONFIGURATION, SOFTWARE_NAME


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_basic(sample_user):
    async with coiled.Cloud(asynchronous=True,) as cloud:

        assert cloud.user == sample_user.user.username
        assert ACCOUNT in cloud.accounts
        assert cloud.default_account == ACCOUNT


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_trailing_slash(ngrok_url, sample_user):
    async with coiled.Cloud(
        server=ngrok_url + "/", asynchronous=True,
    ):
        pass


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_server_input(ngrok_url, sample_user):
    async with coiled.Cloud(
        server=ngrok_url.split("://")[-1], asynchronous=True,
    ) as cloud:
        assert cloud.user == sample_user.user.username
        assert ACCOUNT in cloud.accounts
        assert cloud.default_account == ACCOUNT


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_informative_error_org(ngrok_url, sample_user):
    with pytest.raises(PermissionError) as info:
        async with coiled.Cloud(
            server=ngrok_url.split("://")[-1],
            account="does-not-exist",
            asynchronous=True,
        ):
            pass

    assert sample_user.account.slug in str(info.value)
    assert "does-not-exist" in str(info.value)


@pytest.mark.asyncio
async def test_config(ngrok_url, sample_user):
    async with coiled.Cloud(
        user=sample_user.user.username,
        token=sample_user.user.auth_token.key,
        server=ngrok_url,
        asynchronous=True,
    ) as cloud:
        assert cloud.user == sample_user.user.username
        assert ACCOUNT in cloud.accounts
        assert cloud.default_account == ACCOUNT


@pytest.mark.asyncio
async def test_repr(cloud, ngrok_url, sample_user):
    for func in [str, repr]:
        assert sample_user.user.username in func(cloud)
        assert ngrok_url in func(cloud)


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_informative_errors_on_login(sample_user, clean_configuration):
    with mock.patch("coiled.utils.getpass") as mock_getpass:
        with mock.patch("coiled.utils.input") as mock_input:
            mock_input.side_effect = [sample_user.user.username, "n"]
            mock_getpass.return_value = "foo"
            with pytest.raises(Exception) as info:
                await coiled.Cloud(asynchronous=True)

            assert "Invalid Coiled token" in str(info.value)
            assert mock_getpass.called


@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
def test_sync(sample_user, cluster_configuration):
    with coiled.Cloud() as cloud:
        assert cloud.user == sample_user.user.username
        assert ACCOUNT in cloud.accounts

        with coiled.Cluster(
            configuration=cluster_configuration, cloud=cloud
        ) as cluster:
            assert cluster.scale(1) is None


@pytest.mark.asyncio
async def test_cluster_management(cloud, cluster_configuration, cleanup):
    name = f"myname-{uuid.uuid4().hex}"
    result = await cloud.list_clusters()

    try:
        await cloud.create_cluster(
            configuration=CONFIGURATION, name=name,
        )

        result = await cloud.list_clusters()
        assert name in result

        await cloud.scale(name, n=1)

        async with await coiled.Cluster(name=name, asynchronous=True) as cluster:
            async with Client(cluster, asynchronous=True) as client:
                await client.wait_for_workers(1)

                result = await cloud.list_clusters()
                # Check output is formatted properly
                # NOTE that if we're on AWS the scheduler doesn't really knows its
                # own public address, so we get it from the dashboard link
                if strtobool(environ.get("TEST_AGAINST_AWS", "n")):
                    address = (
                        client.dashboard_link.replace("/status", "")
                        .replace("8787", "8786")
                        .replace("http", "tls")
                    )
                else:
                    address = client.scheduler_info()["address"]

                r = result[name]
                assert r["address"] == address
                # TODO this is returning the id of the configuration.
                # We probably don't want that
                assert isinstance(r["configuration"], int)
                assert r["dashboard_address"] == client.dashboard_link.replace(
                    "/status", ""
                )
                assert r["account"] == ACCOUNT
                assert r["status"] == "running"

    finally:
        await cloud.delete_cluster(name=name)

    # wait for the cluster to shut down
    clusters = await cloud.list_clusters()
    for i in range(5):
        if name not in clusters:
            break
        await asyncio.sleep(1)
        clusters = await cloud.list_clusters()

    assert name not in clusters


@pytest.mark.skip(
    reason="Not working right now, and not critical at the moment. Should not block merging PRs."
)
@pytest.mark.asyncio
async def test_no_aws_credentials_warning(cloud, cluster_configuration, cleanup):
    name = "myname"
    environ["AWS_SHARED_CREDENTIALS_FILE"] = "/tmp/nocreds"
    AWS_ACCESS_KEY_ID = environ.pop("AWS_ACCESS_KEY_ID", None)
    AWS_SECRET_ACCESS_KEY = environ.pop("AWS_SECRET_ACCESS_KEY", None)
    await cloud.create_cluster(
        configuration=CONFIGURATION, name=name,
    )

    with pytest.warns(UserWarning) as records:
        await coiled.Cluster(name=name, asynchronous=True)

    assert (
        records[-1].message.args[0]
        == "No AWS credentials found -- none will be sent to the cluster."
    )
    del environ["AWS_SHARED_CREDENTIALS_FILE"]
    if any((AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)):
        environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY
        environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_default_account(sample_user):
    async with coiled.Cloud(asynchronous=True,) as cloud:
        assert cloud.accounts
        assert cloud.default_account == ACCOUNT


@pytest.mark.asyncio
async def test_cluster_class(cloud, cluster_configuration, cleanup):
    async with coiled.Cluster(
        n_workers=2, asynchronous=True, cloud=cloud, configuration=cluster_configuration
    ) as cluster:
        async with Client(cluster, asynchronous=True, timeout="120 seconds") as client:
            await client.wait_for_workers(2)

            clusters = await cloud.list_clusters()
            assert cluster.name in clusters

    # wait for the cluster to shut down
    clusters = await cloud.list_clusters()
    for i in range(5):
        if cluster.name not in clusters:
            break
        await asyncio.sleep(1)
        clusters = await cloud.list_clusters()

    assert cluster.name not in clusters


@pytest.mark.xfail(reason="We don't support a password keyword currently")
@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)  # implied by `live_server`, but explicit
async def test_password_login(sample_user):
    async with coiled.Cloud(
        sample_user.user.username, password=PASSWORD, asynchronous=True,
    ) as cloud:
        assert PASSWORD not in str(cloud.__dict__)


@pytest.mark.asyncio
async def test_scaling_limits(cloud, cleanup, cluster_configuration, sample_user):
    async with coiled.Cluster(
        configuration=cluster_configuration, asynchronous=True
    ) as cluster:
        with pytest.raises(Exception) as info:
            await cluster.scale(sample_user.membership.limit * 2)

        assert "limit" in str(info.value)
        assert str(sample_user.membership.limit) in str(info.value)
        assert str(sample_user.membership.limit * 2) in str(info.value)


@pytest.mark.xfail(reason="ValueError not being raised for some reason")
@pytest.mark.asyncio
async def test_default_cloud(sample_user, software_env):
    with pytest.raises(Exception) as info:
        cluster = await coiled.Cluster(configuration="foo", asynchronous=True)

    assert "foo" in str(info.value)
    assert "myorg" in str(info.value)

    async with coiled.Cloud(asynchronous=True,):
        async with coiled.Cloud(asynchronous=True,) as cloud_2:
            await cloud_2.create_cluster_configuration(
                name=CONFIGURATION, worker_cpu=1, software=software_env,
            )
            try:
                cluster = coiled.Cluster(configuration=CONFIGURATION, asynchronous=True)
                assert cluster.cloud is cloud_2
            finally:
                await cloud_2.delete_cluster_configuration(name=CONFIGURATION)


@pytest.mark.asyncio
async def test_cloud_repr_html(cloud):
    text = cloud._repr_html_()
    assert cloud.user in text
    assert cloud.server in text
    assert cloud.default_account in text


@pytest.mark.asyncio
async def test_create_and_list_cluster_configuration(
    cloud, cleanup, sample_user, software_env
):
    # TODO decide on defaults and who should own them (defaults in the REST API
    # or maybe just the sdk client)

    # Create basic cluster configuration
    # await cloud.create_cluster_configuration(name="config-1")

    # Create a more customized cluster configuration
    await cloud.create_cluster_configuration(
        name="config-2",
        software=software_env,
        worker_cpu=3,
        worker_memory="3 GiB",
        scheduler_cpu=2,
        scheduler_memory="2 GiB",
        # environment={"foo": "bar"},
    )

    result = await cloud.list_cluster_configurations()

    assert "config-2" in result
    assert result["config-2"]["account"] == ACCOUNT
    assert SOFTWARE_NAME in str(result["config-2"]["scheduler"])
    assert SOFTWARE_NAME in str(result["config-2"]["worker"])

    assert "2" in str(result["config-2"]["scheduler"])
    assert "3" in str(result["config-2"]["worker"])


@pytest.mark.asyncio
async def test_create_and_update_cluster_configuration(
    cloud, cleanup, sample_user, software_env
):
    await cloud.create_cluster_configuration(
        name="config-3",
        software=software_env,
        worker_cpu=3,
        worker_memory="3 GiB",
        scheduler_cpu=2,
        scheduler_memory="2 GiB",
    )
    result = await cloud.list_cluster_configurations()
    assert len(result) == 1
    assert result["config-3"]["scheduler"]["cpu"] == 2
    assert result["config-3"]["worker"]["cpu"] == 3
    assert result["config-3"]["scheduler"]["memory"] == 2

    await cloud.create_cluster_configuration(
        name="config-3",
        software=software_env,
        worker_cpu=4,
        worker_memory="3 GiB",
        scheduler_cpu=4,
        scheduler_memory="3 GiB",
    )
    result = await cloud.list_cluster_configurations()
    assert len(result) == 1
    assert result["config-3"]["scheduler"]["cpu"] == 4
    assert result["config-3"]["worker"]["cpu"] == 4
    assert result["config-3"]["scheduler"]["memory"] == 3


@pytest.mark.asyncio
async def test_delete_cluster_configuration(cloud, cleanup, sample_user, software_env):
    # Initially no configurations
    result = await cloud.list_cluster_configurations()
    assert not result

    # Create two configurations
    await cloud.create_cluster_configuration(
        name="config-1",
        software=software_env,
        worker_cpu=1,
        worker_memory="1 GiB",
        # environment={"foo": "bar"},
    )
    await cloud.create_cluster_configuration(
        name="config-2",
        software=software_env,
        worker_cpu=2,
        worker_memory="2 GiB",
        # environment={"foo": "bar"},
    )

    result = await cloud.list_cluster_configurations()
    assert len(result) == 2

    # Delete one of the configurations
    await cloud.delete_cluster_configuration(name="config-1")
    result = await cloud.list_cluster_configurations()
    assert len(result) == 1
    assert "config-2" in result


@pytest.mark.asyncio
async def test_current(sample_user, clean_configuration):
    with mock.patch("coiled.utils.input") as mock_input:
        with mock.patch("coiled.utils.getpass") as mock_getpass:
            mock_input.side_effect = [sample_user.user.username, "n"]
            mock_getpass.return_value = "foo"
            with pytest.raises(Exception):
                await coiled.Cloud.current()

    with mock.patch("coiled.utils.input") as mock_input:
        with mock.patch("coiled.utils.getpass") as mock_getpass:
            mock_input.side_effect = [sample_user.user.username, "n"]
            mock_getpass.return_value = "foo"
            with pytest.raises(Exception):
                await coiled.Cluster(configuration="default", asynchronous=True)

    with dask.config.set(
        {
            "coiled.cloud.user": sample_user.user.username,
            "coiled.cloud.token": str(sample_user.user.auth_token),
        }
    ):
        await coiled.Cloud.current()
        # await coiled.Cluster(configuration="default", asynchronous=True)  # no cluster config


@pytest.mark.asyncio
async def test_default_org_username(second_user):
    async with coiled.Cloud(asynchronous=True) as cloud:
        assert cloud.default_account == second_user.user.username


@pytest.mark.asyncio
async def test_account_config(sample_user, second_account):
    with dask.config.set({"coiled.cloud.account": second_account.account.slug}):
        async with coiled.Cloud(asynchronous=True,) as cloud:
            assert cloud.default_account == second_account.account.slug


@pytest.mark.asyncio
async def test_list_clusters_account(
    sample_user, second_account, cloud, cluster_configuration
):
    # Create cluster in first account
    await cloud.create_cluster(
        name="cluster-1", configuration=cluster_configuration,
    )

    # Create cluster in second account
    await cloud.create_software_environment(
        name=f"{second_account.account.slug}/env-2", container="daskdev/dask:latest",
    )
    await cloud.create_cluster_configuration(
        name=f"{second_account.account.slug}/config-2", software="env-2",
    )
    await cloud.create_cluster(
        name="cluster-2",
        configuration=f"{second_account.account.slug}/config-2",
        account=second_account.account.slug,
    )

    # Ensure account= in list_clusters filters by the specified account
    result = await cloud.list_clusters(account=second_account.account.slug)
    assert len(result) == 1
    assert "cluster-2" in result


@pytest.mark.asyncio
async def test_connect_to_existing_cluster(cloud, cluster_configuration, cleanup):
    async with coiled.Cluster(
        n_workers=0, asynchronous=True, configuration=cluster_configuration
    ) as a:
        async with coiled.Cluster(asynchronous=True, name=a.name) as b:
            assert a.scheduler_address == b.scheduler_address

        async with Client(a, asynchronous=True):
            pass  # make sure that a is still up


@pytest.mark.asyncio
async def test_connect_same_name(cloud, cluster_configuration, cleanup):
    async with coiled.Cluster(
        name="foo-123",
        n_workers=0,
        asynchronous=True,
        configuration=cluster_configuration,
    ):
        pass

    async with coiled.Cluster(
        name="foo-123",
        n_workers=0,
        asynchronous=True,
        configuration=cluster_configuration,
    ):
        pass


def test_public_api_software_environments(sample_user):
    results = coiled.list_software_environments()
    assert not results

    name = "foo"
    coiled.create_software_environment(name=name, container="daskdev/dask:latest")
    results = coiled.list_software_environments()
    assert len(results) == 1
    assert name in results
    assert results[name]["spec_type"] == "container"
    assert results[name]["spec"] == "daskdev/dask:latest"

    coiled.delete_software_environment(name)
    results = coiled.list_software_environments()
    assert not results


def test_public_api_cluster_configurations(sample_user, software_env):
    results = coiled.list_cluster_configurations()
    assert not results

    name = "foo"
    coiled.create_cluster_configuration(name=name, software=software_env)
    results = coiled.list_cluster_configurations()
    assert len(results) == 1
    assert name in results
    assert (
        results[name]["scheduler"]["software"]
        == f"{sample_user.user.username}/{software_env}"
    )

    coiled.delete_cluster_configuration(name)
    results = coiled.list_cluster_configurations()
    assert not results


def test_public_api_clusters(sample_user, cluster_configuration):
    results = coiled.list_clusters()
    assert not results

    name = "foo"
    coiled.create_cluster(name=name, configuration=cluster_configuration)
    results = coiled.list_clusters()
    assert len(results) == 1
    assert name in results

    coiled.delete_cluster(name)
    results = coiled.list_clusters()
    assert not results


def test_create_cluster_warns(cluster_configuration):
    with pytest.warns(UserWarning, match="use coiled.Cluster()"):
        coiled.create_cluster(name="foo", configuration=cluster_configuration)


@pytest.mark.skip(reason="don't have s3fs on default testing configuration")
@pytest.mark.asyncio
async def test_aws_credentials(cloud, cluster_configuration, cleanup):
    s3fs = pytest.importorskip("s3fs")
    anon = s3fs.S3FileSystem(anon=True)
    try:
        anon.ls("coiled-data")
    except Exception:
        pass
    else:
        raise ValueError("Need to test against private bucket")

    s3 = s3fs.S3FileSystem()
    try:
        s3.ls("coiled-data")
    except Exception as e:
        # no local credentials for private bucket coiled-data
        pytest.skip()

    async with coiled.Cluster(
        n_workers=1, asynchronous=True, configuration=cluster_configuration,
    ) as a:
        async with Client(a, asynchronous=True) as client:

            def f():
                import s3fs

                s3 = s3fs.S3FileSystem()
                return s3.ls("coiled-data")

            await client.submit(f)  # ensure that this doesn't raise
