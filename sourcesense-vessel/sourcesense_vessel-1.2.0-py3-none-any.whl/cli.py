from pyfiglet import Figlet
import click
import time
import os
import sys
import json
from vessel.steps import VaultInitStep, VaultSaveSecretsStep, GenerateKeysStep, \
  RegisterStep, VaultUnsealStep, GenerateYamlStep, DeployAgentStep, DeploySentinelStep
from vessel.pipeline import Pipeline, Payload
from vessel.logging import logger
from vessel.version import VERSION
import kubernetes
from kubernetes.client.rest import ApiException

LATEST_AGENT="1.2"
LATEST_SENTINEL="1.2"

def start(msg):
  click.echo(f"\n> {msg}...")

def end(msg):
  click.echo(f"[*] {msg}")

def prompt(msg, tag, **kwargs):
  return click.prompt(msg, type=str, **kwargs)

@click.group( invoke_without_command=True)
@click.option('--debug', is_flag=True, default=False, help="output debug log [False]")
@click.option('--version', is_flag=True, default=False,  help="Show version and exits")
@click.pass_context
def main(ctx, debug, version):
  """
  Vessel cli tool 
  """
  if version:
    print(f"Vessel cli tool: {VERSION}")
    sys.exit()

  if ctx.invoked_subcommand is None:
    print(ctx.get_help())
    sys.exit()

  click.clear()
  f = Figlet(font='standard')
  click.echo(f.renderText('Vessel cli tool'))
  ctx.ensure_object(dict)
  ctx.obj['DEBUG'] = debug

  if debug:
    logger.setLevel("DEBUG")
  
  # Init directories
  if not os.path.exists(os.path.expanduser("~/.daas")):
      os.mkdir( os.path.expanduser("~/.daas"))

@main.command()
@click.pass_context
@click.option('--vault', default='http://vault.local', help='Vault endpoint [http://vault.local]')
def init(ctx, vault):
  """
  Init vault
  """
  payload = Payload()
  pipeline = Pipeline(start_fn=start, end_fn=end, prompt_fn=prompt)
  pipeline.add(VaultInitStep(vault))
  try:
    # Run pipeline
    payload = pipeline.run(payload)    
  except Exception as e:
    logger.error(e)
    if ctx.obj['DEBUG']:
      raise e

@main.command()
@click.pass_context
@click.option('--vault', default='http://vault.local', help='Vault endpoint [http://vault.local]')
def unseal(ctx, vault):
  """
  Unseal vault
  """
  payload = Payload()
  pipeline = Pipeline(start_fn=start, end_fn=end, prompt_fn=prompt)
  pipeline.add(VaultUnsealStep(vault))
  try:
    # Run pipeline
    payload = pipeline.run(payload)    
  except Exception as e:
    logger.error(e)
    if ctx.obj['DEBUG']:
      raise e

@main.command()
@click.pass_context
@click.argument('token')
@click.option('--cluster-host', required=True, help="Hostname of the cluster to control")
@click.option('--cluster-ro', required=True, help="Cluster read-only service-account token")
@click.option('--cluster-rw', required=True, help="Cluster read-write service-account token")
@click.option('--vault', default='http://vault.local', help='Vault endpoint [http://vault.local]')
@click.option('--openshift', is_flag=True, default=False, help="Cluster is an Openshift distribution [False]")
@click.option('--init', is_flag=True, default=False, help="Initialize Vault [False]")
@click.option('--deploy', is_flag=True, default=False, help="Deploy agent and sentinel container automatically [False]")
@click.option('--vessel-api', default="http://cloud-api.oc.corp.sourcesense.com/rpc", help="Vessel API RPC endpoint [http://cloud-api.oc.corp.sourcesense.com/rpc]")
def register(ctx, token, cluster_host, cluster_ro, cluster_rw, vault, openshift, init, deploy, vessel_api):
  """
  Register workstaion to Vessel with the given TOKEN
  """
  payload = Payload(token)
  pipeline = Pipeline(start_fn=start, end_fn=end, prompt_fn=prompt)
  if init:
    pipeline.add(VaultInitStep(vault))
  pipeline.add(VaultSaveSecretsStep(vault, cluster_host, cluster_ro, cluster_rw, openshift))
  pipeline.add(GenerateKeysStep())
  pipeline.add(RegisterStep(vessel_api))
  pipeline.add(GenerateYamlStep())
  if deploy:
    pipeline.add(DeployAgentStep())
    pipeline.add(DeploySentinelStep())

  try:
    # Run pipeline
    payload = pipeline.run(payload)    
  except Exception as e:
    logger.error(e)
    if ctx.obj['DEBUG']:
      raise e
  

@main.command()
@click.pass_context
@click.argument('token')
@click.option('--dry', is_flag=True, default=False, help="Regenerates yaml files [False]")
def deploy(ctx, token, dry):
  """
  Deploy agent and sentinel for given TOKEN
  """
  click.echo('Debug is %s' % (ctx.obj['DEBUG'] and 'on' or 'off'))
  payload = Payload(token)
  pipeline = Pipeline(start_fn=start, end_fn=end, prompt_fn=prompt)
  pipeline.add(GenerateYamlStep())

  if not dry:
    pipeline.add(DeployAgentStep())
    pipeline.add(DeploySentinelStep())

  try:
    # Run pipeline
    payload = pipeline.run(payload)    
  except Exception as e:
    logger.error(e)
    if ctx.obj['DEBUG']:
      raise e

@main.command()
@click.pass_context
@click.argument('token')
@click.option('--agent-tag', default='latest', help="Set image tag for agent deployment")
@click.option('--sentinel-tag', default='latest', help="Set image tag for sentinel deployment")
def update(ctx, token, sentinel_tag, agent_tag):
  """
  Updates agent and sentinel deployments
  """
  agent_deployment = token + '-agent'
  namespace = 'daas'
  click.echo('Agent deployment name is %s' % agent_deployment)
  click.echo('Updating Sentinel and Agent...')

  # init kube client
  click.echo('Creating kubernetes client configuration...')
  configuration = kubernetes.client.Configuration()
  configuration.host = 'https://localhost:6443'
  configuration.verify_ssl = False
  # TODO: recuperare questo token da vault
  # aprirti il os.path.expanduser(f"~/.daas/vault.json")
  # li dentro hai username e password di vault da utente
  # ti loggi su vault con quelle
  # recuper il token di k8s
  k8s_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IiJ9.eyJpc3MiOiJrdWJlcm5ldGVzL3NlcnZpY2VhY2NvdW50Iiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9uYW1lc3BhY2UiOiJkYWFzIiwia3ViZXJuZXRlcy5pby9zZXJ2aWNlYWNjb3VudC9zZWNyZXQubmFtZSI6ImRlZmF1bHQtdG9rZW4tZnJ0OWsiLCJrdWJlcm5ldGVzLmlvL3NlcnZpY2VhY2NvdW50L3NlcnZpY2UtYWNjb3VudC5uYW1lIjoiZGVmYXVsdCIsImt1YmVybmV0ZXMuaW8vc2VydmljZWFjY291bnQvc2VydmljZS1hY2NvdW50LnVpZCI6ImM0ZDQ0M2IyLWJmOTItNGQ0OS1iZGM5LWJiZjVlZDVkZjM5YiIsInN1YiI6InN5c3RlbTpzZXJ2aWNlYWNjb3VudDpkYWFzOmRlZmF1bHQifQ.WI5UTdoeRpv6E75rYoa7crxNzniqRRDcFeUwR-MPN7y7UM8PjhMpSkTKYafnwV6fOFb2vUDN9qSCwQHNTaKjiQwWQmk4RGfXKxmkWbp3fn8XCltahLjBVvKtr6ZwT0qXS8cL2LSWr5kKruhFzNDefZ8w515jK7zg8PAGtoMz-18sTzdYMfebLVjluPm2AqxFn0WmfDawhqi_UCV4FybUiWYtRLSv0n7SrjAK-xwfISgKamrIdz8x8mCOaQCQ5BrRZuArfJIAIHOy4XUjn5fEurbcql6DcS2aBrq7yfI6ElWG7bZuF4FlsGsntTh8kotesiQ9CbQJC1chr6kZvDACWg'
  configuration.api_key = {"authorization": "Bearer " + k8s_token}
  api_client = kubernetes.client.ApiClient(configuration)
  apps = kubernetes.client.AppsV1Api(api_client)
  
  try:
    body = {
      "spec": {
        "template": {
          "spec": {
            "containers": [
              {
                "name": "593aedda-657e-455b-9491-f774a5006de7-agent",
                "image": "docker-registry.oc.corp.sourcesense.com/daas/workstation-agent:" + agent_tag
                }
            ]
          }
        }
      }
    }
    api_response = apps.patch_namespaced_deployment(agent_deployment, namespace, body)
    logger.debug(api_response)
  except ApiException as e:
    print("Exception when calling AppsV1Api->patch_namespaced_deployment: %s\n" % e)