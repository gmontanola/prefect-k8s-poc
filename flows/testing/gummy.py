from prefect import Flow, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage.github import GitHub


@task(name="Hello World", log_stdout=True)
def hello() -> None:
    print("Olares")


with Flow(
    "gummy",
    storage=GitHub("gmontanola/prefect-k8s-poc", "/flows/testing/gummy.py"),
    run_config=KubernetesRun(labels=["k8s"]),
) as flow:
    hello()
