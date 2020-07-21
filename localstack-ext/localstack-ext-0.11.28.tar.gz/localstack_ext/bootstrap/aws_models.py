from localstack.utils.aws import aws_models
Xfkvu=super
XfkvL=None
Xfkvc=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  Xfkvu(LambdaLayer,self).__init__(arn)
  self.cwd=XfkvL
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,Xfkvc,env=XfkvL):
  Xfkvu(RDSDatabase,self).__init__(Xfkvc,env=env)
 def name(self):
  return self.Xfkvc.split(':')[-1]
class RDSCluster(aws_models.Component):
 def __init__(self,Xfkvc,env=XfkvL):
  Xfkvu(RDSCluster,self).__init__(Xfkvc,env=env)
 def name(self):
  return self.Xfkvc.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
