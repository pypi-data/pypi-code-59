from resource import Resource


class EC2(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrib = kwargs["attrib"]
        self.known_attributes = kwargs["known_attributes"]
        self.output = kwargs["output"]
        self.tag_key = kwargs["tag_key"]
        self.tag_value = kwargs["tag_value"]

    def get_cmd(self):
        cmd = [
            "aws",
            "ec2",
            "describe-instances",
            "--output",
            self.output,
            "--filter",
            f"Name=tag:{self.tag_key},Values={self.tag_value}",
            "--query",
            f"Reservations[*].Instances[*].[{','.join(self.attrib)}]",
        ]

        return cmd

    def get_known_attributes(self):
        return [
            "ImageId",
            "InstanceId",
            "InstanceType",
            "KeyName",
            "LaunchTime",
            "Monitoring.State",
            "Placement.AvailabilityZone",
            "PrivateDnsName",
            "PrivateIpAddress",
            "PublicDnsName",
            "PublicIpAddress",
            "SubnetId",
            "VpcId",
            "BlockDeviceMappings",
            "EbsOptimized",
            "IamInstanceProfile",
            "IamInstanceProfile.Arn",
            "RootDeviceName",
            "RootDeviceType",
            "SecurityGroups",
            "Tags",
            "OwnerId",
        ]
