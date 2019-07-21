#!/usr/bin/env python3

from aws_cdk import core

from stacks import VpcStack

default_tags = {"environment": "dev", "project": "cdk-example"}

app = core.App()

vpc_stack = VpcStack(
    app, "CdkExampleVpcStack", env=dict(region="eu-west-1"), tags=default_tags
)

app.synth()
