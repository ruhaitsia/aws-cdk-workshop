#!/usr/bin/env python3

from aws_cdk import core

from hello.hello_stack import MyStack


app = core.App()
MyStack(app, "hello-cdk-1", env={'account': '','region': ''})
#MyStack(app, "hello-cdk-1", env={'region': 'cn-northwest-1'})
app.synth()
