import Lab2.Lab2 as bmi

def test_bmi_normal_weight():
    result = bmi.calbmi(1.75, 70)
    assert (result == 0)
def test_bmi_underweight():
    result = bmi.calbmi(1.75, 50)
    assert (result == -1)
def test_bmi_overweight():
    result = bmi.calbmi(1.75, 85)
    assert (result == 1)