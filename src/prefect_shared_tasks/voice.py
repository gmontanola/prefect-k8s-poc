from prefect import task


@task(name="Scream", log_stdout=True)
def scream() -> None:
    print("AAAHH!")
