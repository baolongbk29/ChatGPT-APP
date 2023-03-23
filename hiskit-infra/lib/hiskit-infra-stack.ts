import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda";
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class HiskitInfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    
    const layer  = new lambda.LayerVersion(this, "BaseLayer", {
      code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
    });

    const apilambda = new lambda.Function(this, "ApiFunction", {
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app/"),
      handler: "hiskit_api.handler",
      layers: [layer],
    });
  }
}
