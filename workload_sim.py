from typing import Optional

import typer

# Globals
app = typer.Typer()


@app.command()
def session_duration(total_duration: float, num_sessions: int):
    """
    Calculate the average session duration.
    """
    if num_sessions <= 0:
        typer.echo("Number of sessions must be greater than 0.")
        return
    avg_duration = total_duration / num_sessions
    typer.echo(f"Average session duration: {avg_duration:.2f} units")


@app.command()
def inter_arrival_time(total_interval: float, num_intervals: int):
    """
    Calculate the average inter-arrival time between sessions.
    """
    if num_intervals <= 0:
        typer.echo("Number of intervals must be greater than 0.")
        return
    avg_inter_arrival = total_interval / num_intervals
    typer.echo(f"Average inter-arrival time: {avg_inter_arrival:.2f} units")


@app.command()
def total_cpu_load(users: int, requests_per_user: int, cpu_per_request: float):
    """
    Calculate the total CPU load based on active users, requests per user, and CPU usage per request.
    """
    if users <= 0 or requests_per_user <= 0 or cpu_per_request <= 0:
        typer.echo("All inputs must be greater than 0.")
        return
    cpu_load = users * requests_per_user * cpu_per_request
    typer.echo(f"Total CPU Load: {cpu_load:.2f} units")


@app.command()
def total_memory_load(users: int, requests_per_user: int, memory_per_request: float):
    """
    Calculate the total memory load based on active users, requests per user, and memory usage per request.
    """
    if users <= 0 or requests_per_user <= 0 or memory_per_request <= 0:
        typer.echo("All inputs must be greater than 0.")
        return
    memory_load = users * requests_per_user * memory_per_request
    typer.echo(f"Total Memory Load: {memory_load:.2f} units")


@app.command()
def simulate(
    users: int,
    requests_per_user: int,
    cpu_per_request: float,
    memory_per_request: float,
    simulation_scenario: Optional[str] = typer.Option(
        "average", help="Simulation scenario: 'low', 'average', or 'peak'"
    ),
):
    """
    Simulate total load (CPU and Memory) based on the scenario.
    """
    factor = {
        "low": 0.5,
        "average": 1.0,
        "peak": 1.5,
    }.get(simulation_scenario, 1.0)

    cpu_load = users * requests_per_user * cpu_per_request * factor
    memory_load = users * requests_per_user * memory_per_request * factor

    typer.echo(f"Simulation Scenario: {simulation_scenario.capitalize()}")
    typer.echo(f"  Total CPU Load: {cpu_load:.2f} units")
    typer.echo(f"  Total Memory Load: {memory_load:.2f} units")


if __name__ == "__main__":
    app()
