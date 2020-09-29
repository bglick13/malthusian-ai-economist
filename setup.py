import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="-malthusian-ai-economist",
    version="1.1.1",
    author="Ben Glickenhaus, Connor Basich",
    author_email="bglickenhaus@umass.edu",
    description="Foundation: An Economics Simulation Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/salesforce/ai-economist",
    packages=setuptools.find_packages(),
    package_data={
        "ai_economist": ["foundation/scenarios/simple_wood_and_stone/map_txt/*.txt"]},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
