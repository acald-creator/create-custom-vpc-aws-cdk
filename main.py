#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import AwsProvider
from imports.terraform_aws_modules.vpc.aws import Vpc


class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        AwsProvider(self, 'Aws', region='us-east-2')

        Vpc(self, 'PhoenixVeritasCustomVPC',
            name='phoenixveritascustomvpc',
            cidr='13.0.0.0/16',
            azs=["us-east-2a", "us-east-2b", "us-east-2c"],
            public_subnets=["13.0.1.0/24", "13.0.2.0.24"],
            private_subnets=["13.0.3.0/24"]
        )

app = App()
MyStack(app, "create-custom-vpc")

app.synth()
