import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="cdk_example",
    version="0.0.1",
    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "cdk_example"},
    packages=setuptools.find_packages(where="cdk_example"),
    install_requires=["aws-cdk.aws-ec2", "aws-cdk.aws-ecs", "aws-cdk.core", "black"],
    python_requires=">=3.6",
)
