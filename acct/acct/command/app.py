import click
from acct import app_cli, db


@app_cli.command("testdb", help="Test database connection.")
def app_cli_test():
    exit(app_cli_testdb())


def app_cli_testdb():
    try:
        result = db.session.execute("select 1;").first()
        if result[0] == 1:
            click.secho("OK", fg="green", bold=True)
            return 0
        else:
            click.secho("Database connection is OK, but result is not.", fg="yellow")
            return 2
    except:
        click.secho("FAILED", fg="red")
        return 1
