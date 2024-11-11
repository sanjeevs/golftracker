from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="golftracker",
    version="3.0",
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
            'create_swing_db=scripts.create_swing_db:main',
            'dump_swing_db=scripts.dump_swing_db:main',
            'load_swing_db=scripts.load_swing_db:main',
            'display_golf_swing=scripts.display_golf_swing:main',
            'label_club_head=scripts.label_club_head:main',
            'label_golf_poses=scripts.label_golf_poses:main',
            'resize_in_video=scripts.resize_in_video:main',
            'track_golf_club=scripts.track_golf_club:main',
            'create_posemodel=scripts.utils.create_posemodel:main',
            'train_posemodel=scripts.utils.train_posemodel:main',
            'predict_posemodel=scripts.utils.predict_posemodel:main',
            'create_test_image=scripts.utils.create_test_image:main',
            'create_test_db=scripts.utils.create_test_db:main',
            'tune_line_det=scripts.tune_line_det:main',
            'plot_swing_points=scripts.plot_swing_points:main'
        ]
    },
    install_requires = ['opencv-contrib-python', 'protobuf', 'mediapipe', 
                        'numpy', 'scikit-learn', 'pandas'],
    packages = find_packages(),
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    }
)