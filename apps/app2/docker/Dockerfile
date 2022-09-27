FROM python:3.8 as deps
COPY apps.app2/app2.pex /
RUN PEX_TOOLS=1 /usr/local/bin/python3.8 /app2.pex venv --scope=deps --compile /app2

FROM python:3.8 as srcs
COPY apps.app2/app2.pex /
RUN PEX_TOOLS=1 /usr/local/bin/python3.8 /app2.pex venv --scope=srcs --compile /app2

FROM python:3.8
COPY --from=deps /app2 /app2
COPY --from=srcs /app2 /app2

ENTRYPOINT ["/app2/pex"]
