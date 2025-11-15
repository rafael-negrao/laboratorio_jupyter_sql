FROM jupyter/base-notebook:python-3.11

# Evita perguntas interativas na instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências para conectar no PostgreSQL
RUN pip install --no-cache-dir \
    ipython-sql \
    ipywidgets \
    SQLAlchemy \
    psycopg2-binary \
    jupyterlab \
    jupysql

# (Opcional) já iniciar em modo JupyterLab
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.default_url=/lab"]
