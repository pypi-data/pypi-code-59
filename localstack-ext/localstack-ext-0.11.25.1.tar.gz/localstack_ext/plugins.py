import os
SXKdw=Exception
SXKdP=any
SXKdk=str
SXKdv=True
import logging
from localstack import config as localstack_config
from localstack.utils import common
from localstack.constants import(LOCALSTACK_WEB_PROCESS,LOCALSTACK_INFRA_PROCESS,TRUE_STRINGS)
from localstack.utils.bootstrap import is_api_enabled,API_DEPENDENCIES
from localstack_ext import config as config_ext
from localstack_ext.bootstrap import licensing,cli,install,local_daemon
LOG=logging.getLogger(__name__)
def register_localstack_plugins():
 _setup_logging()
 is_infra_process=os.environ.get(LOCALSTACK_INFRA_PROCESS)in TRUE_STRINGS
 if is_infra_process:
  install.install_libs()
  install.setup_ssl_cert()
 if os.environ.get(LOCALSTACK_WEB_PROCESS):
  from localstack_ext.bootstrap.dashboard import dashboard_extended
  dashboard_extended.patch_dashboard()
  return{}
 with licensing.prepare_environment():
  try:
   from localstack_ext.services import dns_server
   dns_server.setup_network_configuration()
  except SXKdw:
   return
  if is_infra_process:
   load_plugin_files()
  try:
   if api_key_configured()and not is_infra_process and is_api_enabled('ec2'):
    local_daemon.start_in_background()
  except SXKdw as e:
   LOG.warning('Unable to start local daemon process: %s'%e)
  if api_key_configured()and not os.environ.get('EDGE_PORT'):
   port=localstack_config.EDGE_PORT
   localstack_config.EDGE_PORT=443
   localstack_config.EDGE_PORT_HTTP=port
 API_DEPENDENCIES['apigateway']=['apigatewayv2']
 API_DEPENDENCIES['emr']=['athena','s3']
 API_DEPENDENCIES['athena']=['emr']
 API_DEPENDENCIES['rds']=['rds-data']
 API_DEPENDENCIES['glacier']=['s3']
 API_DEPENDENCIES['transfer']=['s3']
 API_DEPENDENCIES['elasticache']=['ec2']
 API_DEPENDENCIES['ecs']=['ecr']
 docker_flags=[]
 if config_ext.use_custom_dns():
  if not common.is_port_open(dns_server.DNS_PORT,protocols='tcp'):
   docker_flags+=['-p {a}:{p}:{p}'.format(a=config_ext.DNS_ADDRESS,p=dns_server.DNS_PORT)]
  if not common.is_port_open(dns_server.DNS_PORT,protocols='udp'):
   docker_flags+=['-p {a}:{p}:{p}/udp'.format(a=config_ext.DNS_ADDRESS,p=dns_server.DNS_PORT)]
 EXTERNAL_PORT_APIS=('apigateway','athena','cloudfront','codecommit','ecs','elasticache','mediastore','rds','transfer')
 if SXKdP([is_api_enabled(api)for api in EXTERNAL_PORT_APIS]):
  docker_flags+=['-p {start}-{end}:{start}-{end}'.format(start=config_ext.SERVICE_INSTANCES_PORTS_START,end=config_ext.SERVICE_INSTANCES_PORTS_END)]
 if is_api_enabled('eks'):
  kube_config=os.path.expanduser('~/.kube/config')
  if os.path.exists(kube_config):
   docker_flags+=['-v %s:/root/.kube/config'%kube_config]
 result={'docker':{'run_flags':' '.join(docker_flags)}}
 return result
def load_plugin_files():
 try:
  from localstack.services.plugins import register_plugin,Plugin
  from localstack.services.apigateway import apigateway_listener
  from localstack_ext.services.azure import azure_starter
  from localstack_ext.services.cognito import cognito_starter,cognito_listener
  from localstack_ext.services.sts import sts_starter
  from localstack_ext.services.elasticache import elasticache_starter
  from localstack_ext.services.rds import rds_starter,rds_listener
  from localstack_ext.services.awslambda import lambda_extended
  from localstack_ext.services.ses import ses_starter,ses_listener
  from localstack_ext.services.sqs import sqs_extended
  from localstack_ext.services.sns import sns_extended
  from localstack_ext.services.apigateway import apigateway_extended
  from localstack_ext.services.cloudformation import cloudformation_extended
  from localstack_ext.services.ec2 import ec2_starter,ec2_listener
  from localstack_ext.services.ecr import ecr_starter,ecr_listener
  from localstack_ext.services.ecs import ecs_starter,ecs_listener
  from localstack_ext.services.iot import iot_starter,iot_listener
  from localstack_ext.services.eks import eks_starter
  from localstack_ext.services.emr import emr_starter,emr_listener
  from localstack_ext.services.kms import kms_starter,kms_listener
  from localstack_ext.services.glacier import glacier_starter,glacier_listener
  from localstack_ext.services.xray import xray_starter,xray_listener
  from localstack_ext.services.cloudfront import cloudfront_starter
  from localstack_ext.services.cloudtrail import cloudtrail_starter
  from localstack_ext.services.organizations import organizations_starter
  from localstack_ext.services.athena import athena_starter
  from localstack_ext.services.glue import glue_starter,glue_listener
  from localstack_ext.services.codecommit import codecommit_starter,codecommit_listener
  from localstack_ext.services.qldb import qldb_starter
  from localstack_ext.services.appsync import appsync_starter
  from localstack_ext.services.redshift import redshift_starter,redshift_listener
  from localstack_ext.services.sagemaker import sagemaker_starter
  from localstack_ext.services.stepfunctions import stepfunctions_extended
  from localstack_ext.services.s3 import s3_extended
  from localstack_ext.services.transfer import transfer_starter
  from localstack_ext.services.mediastore import mediastore_starter
  from localstack_ext.services import edge
  from localstack_ext.utils import persistence as persistence_ext
  from localstack_ext.utils.aws import aws_utils
  apigateway_listener.UPDATE_APIGATEWAY.forward_request=cognito_starter.wrap_api_method('apigateway',apigateway_listener.UPDATE_APIGATEWAY.forward_request)
  if os.environ.get('AZURE'):
   register_plugin(Plugin('azure',start=azure_starter.start_azure))
  register_plugin(Plugin('qldb',start=qldb_starter.start_qldb))
  register_plugin(Plugin('rds',start=rds_starter.start_rds,listener=rds_listener.UPDATE_RDS))
  register_plugin(Plugin('sts',start=sts_starter.start_sts))
  register_plugin(Plugin('cognito-idp',start=cognito_starter.start_cognito_idp,listener=cognito_listener.UPDATE_COGNITO))
  register_plugin(Plugin('cognito-identity',start=cognito_starter.start_cognito_identity,listener=cognito_listener.UPDATE_COGNITO_IDENTITY))
  register_plugin(Plugin('elasticache',start=elasticache_starter.start_elasticache))
  register_plugin(Plugin('ec2',start=ec2_starter.start_ec2,listener=ec2_listener.UPDATE_EC2,priority=10))
  register_plugin(Plugin('ecr',start=ecr_starter.start_ecr,listener=ecr_listener.UPDATE_ECR))
  register_plugin(Plugin('ecs',start=ecs_starter.start_ecs,listener=ecs_listener.UPDATE_ECS))
  register_plugin(Plugin('iot',start=iot_starter.start_iot,listener=iot_listener.UPDATE_IOT))
  register_plugin(Plugin('eks',start=eks_starter.start_eks))
  register_plugin(Plugin('emr',start=emr_starter.start_emr,listener=emr_listener.UPDATE_EMR))
  register_plugin(Plugin('kms',start=kms_starter.start_kms,listener=kms_listener.UPDATE_KMS))
  register_plugin(Plugin('xray',start=xray_starter.start_xray,listener=xray_listener.UPDATE_XRAY))
  register_plugin(Plugin('cloudfront',start=cloudfront_starter.start_cloudfront))
  register_plugin(Plugin('athena',start=athena_starter.start_athena))
  register_plugin(Plugin('glacier',start=glacier_starter.start_glacier,listener=glacier_listener.UPDATE_GLACIER))
  register_plugin(Plugin('glue',start=glue_starter.start_glue,listener=glue_listener.UPDATE_GLUE))
  register_plugin(Plugin('codecommit',start=codecommit_starter.start_codecommit,listener=codecommit_listener.UPDATE_CODECOMMIT))
  register_plugin(Plugin('ses',start=ses_starter.start_ses,listener=ses_listener.UPDATE_SES,priority=10))
  register_plugin(Plugin('appsync',start=appsync_starter.start_appsync))
  register_plugin(Plugin('sagemaker',start=sagemaker_starter.start_sagemaker))
  register_plugin(Plugin('cloudtrail',start=cloudtrail_starter.start_cloudtrail))
  register_plugin(Plugin('organizations',start=organizations_starter.start_organizations))
  register_plugin(Plugin('redshift',start=redshift_starter.start_redshift,listener=redshift_listener.UPDATE_REDSHIFT,priority=10))
  register_plugin(Plugin('transfer',start=transfer_starter.start_transfer))
  register_plugin(Plugin('mediastore',start=mediastore_starter.start_mediastore))
  lambda_extended.patch_lambda()
  sns_extended.patch_sns()
  sqs_extended.patch_sqs()
  apigateway_extended.patch_apigateway()
  cloudformation_extended.patch_cloudformation()
  stepfunctions_extended.patch_stepfunctions()
  aws_utils.patch_aws_stack()
  persistence_ext.enable_extended_persistence()
  edge.patch_start_edge()
  s3_extended.patch_s3()
 except SXKdw as e:
  if 'No module named' not in SXKdk(e):
   print(e)
def _setup_logging():
 logging.getLogger('botocore').setLevel(logging.INFO)
 logging.getLogger('kubernetes').setLevel(logging.INFO)
 logging.getLogger('pyftpdlib').setLevel(logging.INFO)
 logging.getLogger('pyhive').setLevel(logging.INFO)
 logging.getLogger('websockets').setLevel(logging.INFO)
 logging.getLogger('asyncio').setLevel(logging.INFO)
 logging.getLogger('hpack').setLevel(logging.INFO)
def api_key_configured():
 return os.environ.get('LOCALSTACK_API_KEY')
def register_localstack_commands():
 if api_key_configured():
  cli.register_commands()
 return SXKdv
# Created by pyminifier (https://github.com/liftoff/pyminifier)
