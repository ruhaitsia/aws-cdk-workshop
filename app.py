#!/usr/bin/env python3

from aws_cdk import core

from crrcopy.crrcopy_stack import MyStack


app = core.App()
MyStack(app, "crrcopy-cdk-1", env={'account': '294739772493','region': 'ap-northeast-1'})
app.synth()
