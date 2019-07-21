#!/usr/bin/env python3

from aws_cdk import core

from stacks import EcsClusterStack

default_tags = {"environment": "dev", "project": "cdk-example"}

app = core.App()

cluster_stack = EcsClusterStack(
    app,
    "CdkExampleClusterStack",
    default_tags,
    vpc_stack.vpc,
    env=dict(region="eu-west-1"),
)

app.synth()
