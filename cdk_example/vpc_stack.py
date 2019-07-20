from aws_cdk import aws_ec2, core


class VpcStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, default_tags, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = aws_ec2.Vpc(self, "Vpc", cidr="10.0.0.0/16", nat_gateways=1)

        for tag in default_tags:
            self.vpc.node.apply_aspect(tag)
