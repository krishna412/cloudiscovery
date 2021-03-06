from pathlib import Path
from typing import List, Dict

from diagrams import Diagram, Cluster, Edge

from shared.common import Resource, ResourceEdge, ResourceDigest
from shared.error_handler import exception

PATH_DIAGRAM_OUTPUT = "./assets/diagrams/"
DIAGRAM_CLUSTER = "diagram_cluster"


class Mapsources:
    # diagrams modules that store classes that represent diagram elements
    diagrams_modules = [
        "analytics",
        "compute",
        "database",
        "devtools",
        "engagement",
        "game",
        "general",
        "integration",
        "iot",
        "management",
        "media",
        "migration",
        "ml",
        "network",
        "robotics",
        "security",
        "storage",
    ]

    # Class to mapping type resource from Terraform to Diagram Nodes
    mapresources = {
        "aws_lambda_function": "Lambda",
        "aws_emr_cluster": "EMRCluster",
        "aws_emr": "EMR",
        "aws_elasticsearch_domain": "ES",
        "aws_msk_cluster": "ManagedStreamingForKafka",
        "aws_sqs_queue_policy": "SQS",
        "aws_instance": "EC2",
        "aws_eks_cluster": "EKS",
        "aws_autoscaling_group": "AutoScaling",
        "aws_ecs_cluster": "ECS",
        "aws_db_instance": "RDS",
        "aws_elasticache_cluster": "ElastiCache",
        "aws_docdb_cluster": "DocumentDB",
        "aws_internet_gateway": "InternetGateway",
        "aws_nat_gateway": "NATGateway",
        "aws_elb_classic": "ELB",
        "aws_elb": "ELB",
        "aws_route_table": "RouteTable",
        "aws_subnet": "PublicSubnet",
        "aws_network_acl": "Nacl",
        "aws_vpc_peering_connection": "VPCPeering",
        "aws_vpc_endpoint_gateway": "Endpoint",
        "aws_iam_policy": "IAMPermissions",
        "aws_iam_user": "User",
        "aws_iam_group": "IAM",
        "aws_iam_role": "IAMRole",
        "aws_iam_instance_profile": "IAM",
        "aws_efs_file_system": "EFS",
        "aws_s3_bucket_policy": "S3",
        "aws_media_connect": "ElementalMediaconnect",
        "aws_media_convert": "ElementalMediaconvert",
        "aws_media_package": "ElementalMediapackage",
        "aws_media_store": "ElementalMediastore",
        "aws_media_tailor": "ElementalMediatailor",
        "aws_media_live": "ElementalMedialive",
        "aws_api_gateway_rest_api": "APIGateway",
        "aws_sagemaker_notebook_instance": "Sagemaker",
        "aws_ssm_document": "SSM",
        "aws_cognito_identity_provider": "Cognito",
        "aws_iot_thing": "InternetOfThings",
        "aws_general": "General",
        "aws_appsync_graphql_api": "Appsync",
        "aws_iot_analytics": "IotAnalytics",
        "aws_securityhub_account": "SecurityHub",
        "aws_trusted_advisor": "TrustedAdvisor",
        "aws_kinesis_firehose": "KinesisDataFirehose",
        "aws_glue": "Glue",
        "aws_quicksight": "Quicksight",
        "aws_cloud9": "Cloud9",
        "aws_organizations_account": "Organizations",
        "aws_config": "Config",
        "aws_auto_scaling": "AutoScaling",
        "aws_backup": "Backup",
        "aws_cloudtrail": "Cloudtrail",
        "aws_cloudwatch": "Cloudwatch",
        "aws_data_pipeline": "DataPipeline",
        "aws_dms": "DMS",
        "aws_elastic_beanstalk_environment": "EB",
        "aws_fms": "FMS",
        "aws_global_accelerator": "GAX",
        "aws_inspector": "Inspector",
        "aws_cloudfront_distribution": "CloudFront",
        "aws_migration_hub": "MigrationHub",
        "aws_sns_topic": "SNS",
        "aws_vpc": "VPC",
        "aws_iot": "IotCore",
        "aws_iot_certificate": "IotCertificate",
        "aws_iot_policy": "IotCertificate",  # TODO: need to fix with new diagram release
        "aws_iot_type": "IotCore",  # TODO: need to fix with new diagram release
        "aws_iot_billing_group": "IotCore",  # TODO: need to fix with new diagram release
        "aws_iot_job": "IotJobs",  # TODO: need to fix with new diagram release
        "aws_alexa": "General",
        "aws_acm": "ACM",
        "aws_mq": "MQ",
        "aws_athena": "Athena",
        "aws_artifact": "Artifact",
        "aws_batch": "Artifact",
        "aws_billingconsole": "General",
        "aws_ce": "General",
        "aws_lex": "Lex",
        "aws_chime": "Lex",
        "aws_clouddirectory": "CloudDirectory",
        "aws_cloudformation": "Cloudformation",
        "aws_cloudhsm": "CloudHSM",
        "aws_cloudsearch": "Cloudsearch",
        "aws_codebuild": "Codebuild",
        "aws_codecommit": "Codecommit",
        "aws_codedeploy": "Codedeploy",
        "aws_codepipeline": "Codepipeline",
        "aws_codestar": "Codestar",
        "aws_discovery": "ApplicationDiscoveryService",
        "aws_dax": "DynamodbDax",
        "aws_deeplens": "Deeplens",
        "aws_delivery_logs": "General",
        "aws_diode": "General",
        "aws_directconnect": "DirectConnect",
        "aws_dlm": "General",
        "aws_ds": "DirectoryService",
        "aws_dynamodb": "Dynamodb",
        "aws_ecr": "EC2ContainerRegistry",
        "aws_efs": "ElasticFileSystemEFS",
        "aws_elastictranscoder": "ElasticTranscoder",
        "aws_events": "Eventbridge",
        "aws_freertos": "FreeRTOS",
        "aws_fsx": "Fsx",
        "aws_gamelift": "Gamelift",
        "aws_glacier": "S3Glacier",
        "aws_greengrass": "Greengrass",
        "aws_guardduty": "Guardduty",
        "aws_health": "General",
        "aws_iam": "IAM",
        "aws_importexport": "General",
        "aws_jellyfish": "General",
        "aws_kinesis": "Kinesis",
        "aws_kinesisanalytics": "KinesisDataAnalytics",
        "aws_kms": "KMS",
        "aws_lakeformation": "LakeFormation",
        "aws_license_manager": "LicenseManager",
        "aws_lightsail": "Lightsail",
        "aws_logs": "General",
        "aws_machinelearning": "MachineLearning",
        "aws_macie": "Macie",
        "aws_managedservices": "General",
        "aws_marketplace": "Marketplace",
        "aws_mobile_hub": "General",
        "aws_monitoring": "General",
        "aws_opsworks": "Opsworks",
        "aws_pinpoint": "Pinpoint",
        "aws_polly": "Polly",
        "aws_qldb": "QLDB",
        "aws_ram": "ResourceAccessManager",
        "aws_redshift": "Redshift",
        "aws_rekognition": "Rekognition",
        "aws_resource_groups": "General",
        "aws_robomaker": "Robomaker",
        "aws_route53": "Route53",
        "aws_s3": "S3",
        "aws_secretsmanager": "SecretsManager",
        "aws_serverlessrepo": "ServerlessApplicationRepository",
        "aws_servicecatalog": "ServiceCatalog",
        "aws_servicediscovery": "General",
        "aws_ses": "SimpleEmailServiceSes",
        "aws_shield": "Shield",
        "aws_signer": "General",
        "aws_signin": "General",
        "aws_sms": "ServerMigrationService",
        "aws_sso": "General",
        "aws_states": "General",
        "aws_storagegateway": "StorageGateway",
        "aws_support": "General",
        "aws_swf": "General",
        "aws_tagging": "General",
        "aws_transfer": "MigrationAndTransfer",
        "aws_translate": "Translate",
        "aws_tts": "General",
        "aws_vmie": "General",
        "aws_waf": "WAF",
        "aws_workdocs": "General",
        "aws_worklink": "General",
        "aws_workmail": "General",
        "aws_workspaces": "General",
        "aws_xray": "XRay",
        "aws_spotfleet": "General",
        "aws_sqs": "SQS",
        "aws_connect": "Connect",
        "aws_iotsitewise": "IotSitewise",
    }


def add_resource_to_group(ordered_resources, group, resource):
    if Mapsources.mapresources.get(resource.digest.type) is not None:
        if group in ordered_resources:
            ordered_resources[group].append(resource)
        else:
            ordered_resources[group] = [resource]


class BaseDiagram(object):
    def __init__(self, name: str, filename: str, engine: str = "sfdp"):
        """
        Class to perform data aggregation, diagram generation and image saving

        The class accepts the following parameters
        :param name:
        :param filename:
        :param engine:
        """
        self.name = name
        self.filename = filename
        self.engine = engine

    def build(self, resources: List[Resource], resource_relations: List[ResourceEdge]):
        self.make_directories()
        self.generate_diagram(resources, resource_relations)

        return self.filename

    @staticmethod
    def make_directories():
        Path(PATH_DIAGRAM_OUTPUT).mkdir(parents=True, exist_ok=True)

    def group_by_group(
        self, resources: List[Resource], initial_resource_relations: List[ResourceEdge]
    ) -> Dict[str, List[Resource]]:
        # Ordering Resource list to group resources into cluster
        ordered_resources: Dict[str, List[Resource]] = dict()
        for resource in resources:
            if Mapsources.mapresources.get(resource.digest.type) is not None:
                if resource.group in ordered_resources:
                    ordered_resources[resource.group].append(resource)
                else:
                    ordered_resources[resource.group] = [resource]
        return ordered_resources

    def process_relationships(
        self,
        grouped_resources: Dict[str, List[Resource]],
        resource_relations: List[ResourceEdge],
    ) -> List[ResourceEdge]:
        return resource_relations

    @exception
    def generate_diagram(
        self, resources: List[Resource], initial_resource_relations: List[ResourceEdge]
    ):
        ordered_resources = self.group_by_group(resources, initial_resource_relations)
        relations = self.process_relationships(
            ordered_resources, initial_resource_relations
        )

        with Diagram(
            name=self.name,
            filename=PATH_DIAGRAM_OUTPUT + self.filename,
            direction="TB",
            graph_attr={"nodesep": "2.0", "ranksep": "1.0", "splines": "curved"},
        ) as d:
            d.dot.engine = self.engine

            self.draw_diagram(ordered_resources=ordered_resources, relations=relations)

    def draw_diagram(self, ordered_resources, relations):
        already_drawn_elements = {}

        # Import all AWS nodes
        for module in Mapsources.diagrams_modules:
            exec("from diagrams.aws." + module + " import *")

        nodes: Dict[ResourceDigest, any] = {}
        # Iterate resources to draw it
        for group_name in ordered_resources:
            if group_name == "":
                for resource in ordered_resources[group_name]:
                    node = eval(Mapsources.mapresources.get(resource.digest.type))(
                        resource.name
                    )
                    nodes[resource.digest] = node
            else:
                with Cluster(group_name.capitalize() + " resources") as cluster:
                    nodes[ResourceDigest(id=group_name, type=DIAGRAM_CLUSTER)] = cluster
                    for resource in ordered_resources[group_name]:
                        node = eval(Mapsources.mapresources.get(resource.digest.type))(
                            resource.name
                        )
                        nodes[resource.digest] = node

        for resource_relation in relations:
            if resource_relation.from_node == resource_relation.to_node:
                continue
            if (
                resource_relation.from_node in nodes
                and resource_relation.to_node in nodes
            ):
                from_node = nodes[resource_relation.from_node]
                to_node = nodes[resource_relation.to_node]
                if resource_relation.from_node not in already_drawn_elements:
                    already_drawn_elements[resource_relation.from_node] = {}
                if (
                    resource_relation.to_node
                    not in already_drawn_elements[resource_relation.from_node]
                ):
                    from_node >> Edge(label=resource_relation.label) >> to_node
                    already_drawn_elements[resource_relation.from_node][
                        resource_relation.to_node
                    ] = True


class NoDiagram(BaseDiagram):
    def __init__(self):
        """
        Special class that doesn't generate any image.

        Command should be refactored not to have such class
        """
        super().__init__("", "")

    def generate_diagram(
        self, resources: List[Resource], resource_relations: List[ResourceEdge]
    ):
        pass

    def build(self, resources: List[Resource], resource_relations: List[ResourceEdge]):
        pass
