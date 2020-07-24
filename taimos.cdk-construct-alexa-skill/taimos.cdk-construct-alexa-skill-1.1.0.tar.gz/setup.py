import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "taimos.cdk-construct-alexa-skill",
    "version": "1.1.0",
    "description": "An AWS CDK Construct that creates an Alexa Skill backend",
    "license": "Apache-2.0",
    "url": "https://github.com/taimos/cdk-construct-alexa-skill",
    "long_description_content_type": "text/markdown",
    "author": "Thorsten Hoeger<thorsten.hoeger@taimos.de>",
    "project_urls": {
        "Source": "https://github.com/taimos/cdk-construct-alexa-skill"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "taimos.cdk_construct_alexa_skill",
        "taimos.cdk_construct_alexa_skill._jsii"
    ],
    "package_data": {
        "taimos.cdk_construct_alexa_skill._jsii": [
            "cdk-construct-alexa-skill@1.1.0.jsii.tgz"
        ],
        "taimos.cdk_construct_alexa_skill": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "jsii>=1.9.0, <2.0.0",
        "publication>=0.0.3",
        "aws-cdk.aws-dynamodb==1.54.0",
        "aws-cdk.aws-iam==1.54.0",
        "aws-cdk.aws-lambda==1.54.0",
        "aws-cdk.aws-s3==1.54.0",
        "aws-cdk.core==1.54.0",
        "constructs==3.0.4"
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
