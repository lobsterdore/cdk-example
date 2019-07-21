from aws_cdk import aws_ecs, core


class EcsClusterStack(core.Stack):
    def __init__(
        self, scope: core.Construct, id: str, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.cluster = aws_ecs.Cluster(
            self, "Cluster", cluster_name="cdk-example", vpc=vpc
        )
