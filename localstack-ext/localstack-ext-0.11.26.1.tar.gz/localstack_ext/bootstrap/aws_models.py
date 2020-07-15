from localstack.utils.aws import aws_models
ficDA=super
ficDP=None
ficDq=id
class LambdaLayer(aws_models.LambdaFunction):
 def __init__(self,arn):
  ficDA(LambdaLayer,self).__init__(arn)
  self.cwd=ficDP
  self.runtime=''
  self.handler=''
  self.envvars={}
  self.versions={}
class RDSDatabase(aws_models.Component):
 def __init__(self,ficDq,env=ficDP):
  ficDA(RDSDatabase,self).__init__(ficDq,env=env)
 def name(self):
  return self.ficDq.split(':')[-1]
class RDSCluster(aws_models.Component):
 def __init__(self,ficDq,env=ficDP):
  ficDA(RDSCluster,self).__init__(ficDq,env=env)
 def name(self):
  return self.ficDq.split(':')[-1]
# Created by pyminifier (https://github.com/liftoff/pyminifier)
