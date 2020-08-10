import pytest
from acct import db


@pytest.mark.run(order=1)
def test_database_connection(app):
    with app.app_context():
        try:
            result = db.session.execute("select 1;").first()
            assert result[0] == 1
        except:
            assert 0
