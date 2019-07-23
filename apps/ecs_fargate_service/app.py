#!/usr/bin/env python3

from aws_cdk import core

from stacks import EcsFargateService

env_config = {
    "default_tags": {"environment": "dev", "project": "cdk-example"},
    "region": "eu-west-1"
}

app = core.App()

EcsFargateService(
    app,
    "CdkExampleFargateStack",
    env=dict(region=env_config["region"], account="920609328416"),
    env_config=env_config,
    tags=env_config["default_tags"]
)

app.synth()
