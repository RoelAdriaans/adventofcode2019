from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="adventofcode2019",
    author="Roel Adriaans",
    author_email="roel@adriaans.org",
    url="https://github.com/roeladriaans",
    entry_points={"console_scripts": ["adventofcode = adventofcode2019.main:main"]},
    packages=find_packages(where="src", exclude=["tests.*", "test*"]),
    package_dir={"": "src"},
    install_requires=requirements,
    include_package_data=True,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
