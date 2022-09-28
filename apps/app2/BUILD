python_requirement(name="setproctitle_req", requirements=["setproctitle"])

pex_binary(
    name="app2",
    entry_point="src/app2/main.py",
    include_tools=True,
    dependencies=[":setproctitle_req"],
)

resource(name="readme", source="README.md")
