import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (
    aws_ec2 as ec2,
)

class ListNATGatewaysPerVPCStack(cdk.Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # List all VPCs
        vpcs = ec2.Vpc.list_vpcs(self)

        # Iterate through each VPC and list its NAT gateways
        for vpc in vpcs:
            print(f"VPC ID: {vpc.vpc_id}")
            nat_gateways = vpc.nat_gateways
            for nat_gateway in nat_gateways:
                print(f"  NAT gateway ID: {nat_gateway.nat_gateway_id}")
