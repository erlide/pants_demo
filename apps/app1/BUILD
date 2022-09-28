python_requirement(name="setproctitle_req", requirements=["setproctitle"])

pex_binary(
    name="app1",
    entry_point="src/app1/other.py:enter",
    include_tools=True,
    dependencies=[":setproctitle_req"],
)

resource(name="readme", source="README.md")
