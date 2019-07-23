from aws_cdk import aws_ec2, aws_ecs, core


class EcsClusterStack(core.Stack):
    def __init__(
        self, scope: core.Construct, id: str,  env_config: dict, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = aws_ec2.Vpc.from_lookup(self, 'Vpc', tags={"tag:environment": "dev", "tag:project": "cdk-example"})

        self.cluster = aws_ecs.Cluster(
            self, "Cluster", cluster_name="cdk-example", vpc=vpc
        )
