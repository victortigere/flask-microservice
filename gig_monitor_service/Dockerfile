FROM python:3.9.15-alpine3.16
WORKDIR /app
COPY requirements.txt .
RUN pip install -r ./requirements.txt
COPY src src
EXPOSE 5002
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
            CMD curl -f http://localhost:5002/monitor/health || exit 1
ENTRYPOINT [ "python", "./src/app.py" ]