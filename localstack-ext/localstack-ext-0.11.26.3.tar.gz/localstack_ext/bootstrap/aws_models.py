from localstack.utils.aws import aws_models
uQcAi=super
uQcAU=None
uQcAz=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  uQcAi(LambdaLayer,self).__init__(arn)
  self.cwd=uQcAU
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,uQcAz,env=uQcAU):
  uQcAi(RDSDatabase,self).__init__(uQcAz,env=env)
 def name(self):
  return self.uQcAz.split(':')[-1]
class RDSCluster(aws_models.Component):
 def __init__(self,uQcAz,env=uQcAU):
  uQcAi(RDSCluster,self).__init__(uQcAz,env=env)
 def name(self):
  return self.uQcAz.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
