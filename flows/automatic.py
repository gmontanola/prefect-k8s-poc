from prefect import Flow, task
from prefect.run_configs.kubernetes import KubernetesRun
from prefect.storage.github import GitHub


@task(name="Sucesso", log_stdout=True)
def message() -> None:
    print("Essa flow foi registrada com GitHub Actions!")


with Flow(
    "automatic-registering",
    storage=GitHub("gmontanola/prefect-k8s-poc", "/flows/automatic.py"),
    run_config=KubernetesRun(labels=["k8s"]),
) as flow:
    message()
