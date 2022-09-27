resource(name="pyproject", source="pyproject.toml")

python_distribution(
    name="lib2",
    dependencies=[
        ":pyproject",
        # Dependencies on code to be packaged into the distribution.
        "libs/lib2/src/lib2",
    ],
    provides=python_artifact(
        name="lib2",
        version="2.21.0",
    ),
    # Example of setuptools config, other build backends may have other config.
    wheel_config_settings={"--global-option": ["--python-tag", "py37.py38.py39"]},
    # Don't use setuptools with a generated setup.py.
    # You can also turn this off globally in pants.toml:
    #
    # [setup-py-generation]
    # generate_setup_default = false
    generate_setup=True,
)
