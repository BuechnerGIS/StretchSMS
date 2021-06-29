from StretchSMS import CARRIERS

def test_phone_number():
    assert '1234567890'.isnumeric()
    assert not '123-456-7890'.isnumeric()

def test_carrier():
    assert 'verizon' in CARRIERS.keys()
    assert not 'mymobilecompany' in CARRIERS.keys()
