from setuptools import setup, find_packages

setup(
    name="model_deployment",
    version="0.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="A project for model deployment in two modes: online (REST API) and batch (scheduled pipeline)",
    url="https://github.com/yourusername/model_deployment",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flask>=2.0.0",
        "requests>=2.25.0",
        "scikit-learn>=0.24.0",
        "pandas>=1.2.0",
        "joblib>=1.0.0",
        "pytest>=6.0.0",
        "numpy>=1.19.0"
    ],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)