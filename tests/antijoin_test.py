import pytest
import pandas as pd
from reframe import Relation

@pytest.fixture(scope="module")
def r():
    data_real = {"name": ["Carol", "Bob", "Damien"], "age": [86, 4, 400]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)


def test_foo(r):
    data_test = {"name": ["Carol","Bob"], "age": [86,4]}
    df_test = pd.DataFrame(data=data_test)
    r_test = Relation(df_test)
    print("Original\n",r)
    print("test data\n",r_test)
    
    r_aj = r.antijoin(r_test).project(['name','age'])
    r_expected = Relation("tests/test_antijoin_expected_1.csv", sep="|").project(['name','age'])
    print("antijoin\n",r_aj)
    print("Expected:\n",r_expected)
    
    assert r_aj.equals(r_expected)


# def test_foo_2(r):
#     r = r.project(["name"])
#     r_expected_2 = Relation("tests/test_project_expected_1.csv", sep="|")
#     assert r.equals(r_expected_2)