#!/usr/bin/env python3

from aws_cdk import core

from cdk_trial.cdk_trial_stack import CdkTrialStack


app = core.App()
CdkTrialStack(app, "cdk-trial")

app.synth()
