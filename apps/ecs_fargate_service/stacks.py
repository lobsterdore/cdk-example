from aws_cdk import aws_ec2, aws_ecs, core


class EcsFargateService(core.Stack):
    def __init__(
        self, scope: core.Construct, id: str, env_config: dict, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = aws_ec2.Vpc.from_lookup(self, 'Vpc', tags={"tag:environment": "dev", "tag:project": "cdk-example"})


        cluster = aws_ecs.Cluster.from_cluster_attributes(self, 'Cluster',
            cluster_name='cdk-example', vpc=vpc)

        task_definition = aws_ecs.FargateTaskDefinition(
            self, "TaskDefinition", cpu=256, memory_limit_mib=512
        )

        container = task_definition.add_container(
            "nginx", image=aws_ecs.ContainerImage.from_registry("nginx:latest")
        )

        container.add_port_mappings(
            aws_ecs.PortMapping(container_port=80, protocol=aws_ecs.Protocol.TCP)
        )

        security_group = aws_ec2.SecurityGroup(
            self, "cdk-fargate-example", vpc=vpc
        )
        security_group.add_ingress_rule(
            aws_ec2.Peer.ipv4(vpc.vpc_cidr_block), aws_ec2.Port.tcp(80)
        )

        service = aws_ecs.FargateService(
            self,
            "FargateService",
            cluster=cluster,
            security_group=security_group,
            service_name="cdk-fargate-example",
            task_definition=task_definition,
            vpc_subnets={"subnetType": aws_ec2.SubnetType.PRIVATE},
        )

        # for resource in [task_definition, security_group, service]:
        #     for tag in default_tags:
        #         resource.node.apply_aspect(tag)
