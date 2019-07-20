#!/usr/bin/env python3

from aws_cdk import core

from cdk_example.ecs_cluster_stack import EcsClusterStack
from cdk_example.ecs_fargate_service import EcsFargateService
from cdk_example.vpc_stack import VpcStack

default_tags = [core.Tag("environment", "dev"), core.Tag("project", "cdk-example")]

app = core.App()

vpc_stack = VpcStack(
    app, "CdkExampleVpcStack", default_tags, env=dict(region="eu-west-1")
)

cluster_stack = EcsClusterStack(
    app,
    "CdkExampleClusterStack",
    default_tags,
    vpc_stack.vpc,
    env=dict(region="eu-west-1"),
)

EcsFargateService(
    app,
    "CdkExampleFargateStack",
    default_tags,
    vpc_stack.vpc,
    cluster_stack.cluster,
    env=dict(region="eu-west-1"),
)

app.synth()
