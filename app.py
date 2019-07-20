#!/usr/bin/env python3

from aws_cdk import core

from cdk_example.vpc_stack import VpcStack


app = core.App()
VpcStack(app, "CdkVpcStack")

app.synth()
