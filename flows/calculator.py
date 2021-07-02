from prefect import Flow, Parameter, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage.github import GitHub


@task(name="Calculadora tosca", log_stdout=True)
def dumb_sumb(x: int, y: int) -> None:
    print(f"{x} + {y} = {x+y}")


with Flow(
    "calculator",
    storage=GitHub("gmontanola/prefect-k8s-poc", "/flows/calculator.py"),
    run_config=KubernetesRun(labels=["k8s"]),
) as flow:
    x = Parameter(name="x value")
    y = Parameter(name="y value")
    dumb_sumb(x, y)
