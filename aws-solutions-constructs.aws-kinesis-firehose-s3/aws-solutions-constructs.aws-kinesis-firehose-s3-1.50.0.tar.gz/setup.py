import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws-solutions-constructs.aws-kinesis-firehose-s3",
    "version": "1.50.0",
    "description": "CDK constructs for defining an interaction between an Amazon Kinesis Data Firehose delivery stream and an Amazon S3 bucket.",
    "license": "Apache-2.0",
    "url": "https://github.com/awslabs/aws-solutions-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "project_urls": {
        "Source": "https://github.com/awslabs/aws-solutions-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_solutions_constructs.aws_kinesis_firehose_s3",
        "aws_solutions_constructs.aws_kinesis_firehose_s3._jsii"
    ],
    "package_data": {
        "aws_solutions_constructs.aws_kinesis_firehose_s3._jsii": [
            "aws-kinesisfirehose-s3@1.50.0.jsii.tgz"
        ],
        "aws_solutions_constructs.aws_kinesis_firehose_s3": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii>=1.8.0, <2.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-iam>=1.50.0, <1.51.0",
        "aws-cdk.aws-kinesisfirehose>=1.50.0, <1.51.0",
        "aws-cdk.aws-logs>=1.50.0, <1.51.0",
        "aws-cdk.aws-s3>=1.50.0, <1.51.0",
        "aws-cdk.core>=1.50.0, <1.51.0",
        "aws-solutions-constructs.core>=1.50.0, <1.51.0",
        "constructs>=3.0.2, <4.0.0"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
        "License :: OSI Approved"
    ]
}
"""
)

with open("README.md") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
