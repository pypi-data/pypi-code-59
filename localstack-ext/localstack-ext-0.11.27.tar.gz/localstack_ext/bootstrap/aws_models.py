from localstack.utils.aws import aws_models
KyLSq=super
KyLSp=None
KyLSc=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  KyLSq(LambdaLayer,self).__init__(arn)
  self.cwd=KyLSp
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,KyLSc,env=KyLSp):
  KyLSq(RDSDatabase,self).__init__(KyLSc,env=env)
 def name(self):
  return self.KyLSc.split(':')[-1]
class RDSCluster(aws_models.Component):
 def __init__(self,KyLSc,env=KyLSp):
  KyLSq(RDSCluster,self).__init__(KyLSc,env=env)
 def name(self):
  return self.KyLSc.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
