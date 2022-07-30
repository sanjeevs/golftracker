from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="golftracker",
    version="0.0.7",
    description="Use open cv to detect critical elements in a golf swing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    url="https://github.com/sanjeevs/golftracker",
    author="Sanjeev Singh",
    author_email="snjvsingh123@gmail.com",
    entry_points={
        'console_scripts' : [
            'golfeditor=golftracker.golfeditor:main',
            'merge_setup=golftracker.merge_setup:main',
            'modelview=golftracker.modelview:main',
            'pose_detection=golftracker.pose_detection:main'
        ]
    },
    install_requires = ['opencv-contrib-python', 'protobuf==3.20.0', 'mediapipe==0.8.10'],
    packages = ['golftracker'],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    }
)