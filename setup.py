import setuptools

with open("README.md", "r", encoding="utf-8") as f:  # read your read me file
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "2nd-E-E-MLOps-and-Deployment-Text-Summarization-"  #give your repo name
AUTHOR_USER_NAME = "Daniel Jackson"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "arcdaniel20@gmail.com"


#the below code will loook for the construtor file ane install it
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This is My second project and my first small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)