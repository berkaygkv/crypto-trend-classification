import mlflow
from nbconvert import HTMLExporter
from sklearn_evaluation import NotebookIntrospector

# HTMLExporter
def store_report(product, params):
    if params['track']:
        nb = NotebookIntrospector(product)
        run_id = nb['mlflow-run-id'].strip()

        exporter = HTMLExporter()
        # hide code cells
        exporter.exclude_input = True
        body, _ = exporter.from_filename(product)

        with mlflow.start_run(run_id):
            mlflow.log_text(body, 'nb.html')