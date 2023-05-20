"""
    :copyright: © 2020 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from __init__ import app 


def test_gpt_apt():
    with app.test_client() as c:
        rv = c.post(
            "/v1/gpt_text/normal_gpt",
            headers={},
            json={
                "query": "What is my last question?",
            },
        )
        print(rv.get_json(), flush=True)

if __name__ == "__main__":
    test_gpt_apt()

