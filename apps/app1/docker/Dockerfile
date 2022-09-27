FROM python:3.8 as deps
COPY apps.app1/app1.pex /
RUN PEX_TOOLS=1 /usr/local/bin/python3.8 /app1.pex venv --scope=deps --compile /app1

FROM python:3.8 as srcs
COPY apps.app1/app1.pex /
RUN PEX_TOOLS=1 /usr/local/bin/python3.8 /app1.pex venv --scope=srcs --compile /app1

FROM python:3.8
COPY --from=deps /app1 /app1
COPY --from=srcs /app1 /app1

ENTRYPOINT ["/app1/pex"]
