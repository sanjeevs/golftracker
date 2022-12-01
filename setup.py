from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="golftracker",
    version="1.0.0",
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
            'create_stick_video=scripts.create_stick_video:main',
            'create_golf_db=scripts.create_golf_db:main',
            'display_golf_swing=scripts.display_golf_swing:main',
            'label_poses=scripts.label_poses:main',
            'create_posemodel=scripts.create_posemodel:main',
            'train_posemodel=scripts.train_posemodel:main',
            'predict_posemodel=scripts.predict_posemodel:main',
            'create_test_image=scripts.create_test_image:main'
        ]
    },
    install_requires = ['opencv-contrib-python', 'protobuf==3.20.0', 'mediapipe==0.8.10', 
                        'numpy', 'scikit-learn', 'pandas'],
    packages = ['golftracker'],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    }
)