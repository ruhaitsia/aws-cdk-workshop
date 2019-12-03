from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    aws_s3 as _s3,
    aws_s3_deployment as _s3_deployment,
    aws_s3_notifications as _s3_notifications,
    aws_iam as _iam
)

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # lambdaRole = _iam.Role(
        #     self,'lambdaRole',
        #     role_name= 'lambda_crr_s3_role',
        #     assumed_by= _iam.ServicePrincipal('lambda.amazonaws.com')
        # )
        #
        #
        # lambdaRole.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name('AWSLambdaFullAccess'))
        # lambdaRole.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonS3FullAccess'))
        # lambdaRole.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name('CloudWatchFullAccess'))
        # lambdaRole.add_managed_policy(_iam.ManagedPolicy.from_aws_managed_policy_name('AmazonDynamoDBFullAccess'))
        #
        # S3MPU = ddb.Table(
        #     self, 'S3MPU',
        #     table_name='S3MPU',
        #     partition_key={'name': 'uploadid', 'type': ddb.AttributeType.STRING},
        #     sort_key={'name': 'part', 'type' : ddb.AttributeType.NUMBER}
        # )
        #
        # S3MPUResult = ddb.Table(
        #     self, 'S3MPUResult',
        #     table_name='S3MPUResult',
        #     partition_key={'name': 'uploadid', 'type': ddb.AttributeType.STRING}
        # )
        #
        # S3Single = ddb.Table(
        #     self, 'S3Single',
        #     table_name='S3Single',
        #     partition_key={'name': 'id', 'type': ddb.AttributeType.STRING}
        # )
        #
        # S3SingleResult = ddb.Table(
        #     self, 'S3SingleResult',
        #     table_name='S3SingleResult',
        #     partition_key={'name': 'id', 'type': ddb.AttributeType.STRING}
        # )
        #
        # sourceBucket = _s3.Bucket(self,"CredBucket")
        #
        # _s3_deployment.BucketDeployment(self, "DeployCredential",
        #                           sources=[_s3_deployment.Source.asset("credential")],
        #                           destination_bucket=sourceBucket
        #                           )
        #
        # S3CopyToChinaMain = _lambda.Function(
        #     self, 'S3CopyToChina-Main',
        #     runtime=_lambda.Runtime.PYTHON_3_6,
        #     handler='S3CopyToChina-Main.lambda_handler',
        #     function_name= 'S3CopyToChina-Main',
        #     code=_lambda.Code.asset('lambda'),
        #     role= lambdaRole,
        #     timeout= core.Duration.minutes(5),
        #     environment={
        #         'DstBucket': 's3-crr-zhy',
        #         'CredBucket': sourceBucket.bucket_name,
        #         'CredObject': 'S3BJScredential.txt'
        #     }
        # )
        #
        # S3CopyToChinaMonitor = _lambda.Function(
        #     self, 'S3CopyToChina-Monitor',
        #     runtime=_lambda.Runtime.PYTHON_3_6,
        #     handler='S3CopyToChina-Monitor.lambda_handler',
        #     function_name='S3CopyToChina-Monitor',
        #     code=_lambda.Code.asset('lambda'),
        #     role=lambdaRole,
        #     timeout=core.Duration.minutes(5)
        # )
        #
        # S3CopyToChinaMPU = _lambda.Function(
        #     self, 'S3CopyToChina-MPU',
        #     runtime=_lambda.Runtime.PYTHON_3_6,
        #     handler='S3CopyToChina-MPU.lambda_handler',
        #     function_name='S3CopyToChina-MPU',
        #     code=_lambda.Code.asset('lambda'),
        #     role=lambdaRole,
        #     timeout=core.Duration.minutes(5),
        #     environment={
        #         'CredBucket': sourceBucket.bucket_name,
        #         'CredObject': 'S3BJScredential.txt'
        #     }
        # )
        #
        # S3CopyToChinaSingle = _lambda.Function(
        #     self, 'S3CopyToChina-Single',
        #     runtime=_lambda.Runtime.PYTHON_3_6,
        #     handler='S3CopyToChina-Single.lambda_handler',
        #     function_name='S3CopyToChina-Single',
        #     code=_lambda.Code.asset('lambda'),
        #     role=lambdaRole,
        #     timeout=core.Duration.minutes(5),
        #     environment={
        #         'CredBucket': sourceBucket.bucket_name,
        #         'CredObject': 'S3BJScredential.txt'
        #     }
        # )
        #
        # notification = _s3_notifications.LambdaDestination(S3CopyToChinaMain)
        #
        # sourceBucket.add_event_notification(_s3.EventType.OBJECT_CREATED, notification)
        #
        # sourceBucket.add_event_notification(_s3.EventType.OBJECT_REMOVED, notification)