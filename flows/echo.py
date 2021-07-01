from prefect import Flow, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage.github import GitHub


@task(name="Hello World", log_stdout=True)
def hello() -> None:
    print("Olá mundo! Estou com frio...")


with Flow(
    "hello-world",
    storage=GitHub("gmontanola/prefect-k8s-poc", "/flows/echo.py"),
    run_config=KubernetesRun(labels=["k8s"]),
) as flow:
    hello()
