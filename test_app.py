from app import add
def add_test_positive():
  assert add(2,3) == 5
def add_test_negative():
  assert add(-1,-1) == -2
def add_test_zero():
  assert add(0,5) == 5
def add_test_mixed():
  assert add(-1,1) == 0
def test_output_type():
  result = add(10,5)
  assert isinstance(result,int)
  assert result == 15
