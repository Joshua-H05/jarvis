from jarvis import preprocessing as p
import pandas as pd
import pysnooper


"""def test_one_hot():
    df = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached']
    })
    expected = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached'],
        "Gender_Female": [1, 0, 0, 1, 1],
        "Gender_Male": [0, 1, 1, 0, 0],
    })
    result = p.one_hot(df, "Gender")
    assert result.equals(expected)"""


def test_drop_col():
    df = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached']
    })
    expected = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached'],

    })
    result = p.rm_col(df, "Gender")
    assert result.equals(expected)


def test_drop_col_mul():
    df = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached']
    })
    expected = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi']
    })
    result = p.rm_col(df, "Gender", "House Type")
    assert result.equals(expected)


def test_drop_row():
    df = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached']
    })
    expected = pd.DataFrame({
        'Name': ['Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Male', 'Male', 'Female', 'Female'],
        'House Type': ['Detached', 'Apartment', None, 'Semi-Detached']
    })
    result = p.rm_row(df, [0])
    print(f"{result}\n")
    print(expected)
    assert result.equals(expected)


def test_drop_row_mul():
    df = pd.DataFrame({
        'Name': ['Joan', 'Matt', 'Jeff', 'Melissa', 'Devi'],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'House Type': ['Apartment', 'Detached', 'Apartment', None, 'Semi-Detached']
    })
    expected = pd.DataFrame({
        'Name': ['Jeff', 'Melissa', 'Devi'],
        'Gender': ['Male', 'Female', 'Female'],
        'House Type': ['Apartment', None, 'Semi-Detached']
    })
    result = p.rm_row(df, [0, 1])
    print(f"{result}\n")
    print(expected)
    assert result.equals(expected)


@pysnooper.snoop(depth=2)
def test_add():
    df = pd.DataFrame([(.21, .32), (.01, .67), (.66, .03), (.21, .18)], columns=['dogs', 'cats'])
    result = p.operation(df=df, name="sum", operator="+", col1="dogs", col2="cats")
    expected = pd.DataFrame([(.21, .32, .53),
                             (.01, .67, .68),
                             (.66, .03, .69),
                             (.21, .18, .39)],
                            columns=['dogs', 'cats', "sum"])
    print(result)
    print(expected)
    assert result.equals(expected)


