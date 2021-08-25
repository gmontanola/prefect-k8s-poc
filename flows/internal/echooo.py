from prefect import Flow, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage.github import GitHub

from prefect_shared_tasks.voice import scream


@task(name="Hello World", log_stdout=True)
def hello() -> None:
    print("3")


with Flow(
    "hello-world-3",
    storage=GitHub("gmontanola/prefect-k8s-poc", "/flows/echooo.py"),
    run_config=KubernetesRun(labels=["k8s"]),
) as flow:
    hello()
    scream()
