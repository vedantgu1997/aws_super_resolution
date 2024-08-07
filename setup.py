import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

version = "0.1.0"

REPO_NAME = 'aws_super_resolution'
AUTHOR_USER_NAME = 'vedantgu1997'
SRC_REPO = 'superResolution'

setuptools.setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_USER_NAME,
    description="A package for super resolution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
