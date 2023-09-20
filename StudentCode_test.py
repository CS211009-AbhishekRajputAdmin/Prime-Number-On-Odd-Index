import StudentCode;
from IOWrapper import IOWrapper
testIO= IOWrapper()
expectedIO= IOWrapper()
expectedIO1= IOWrapper()
def test_hello():
    expectedIO.print("Prime Number")
    expectedIO1.print("Not Prime Number")
    assert (StudentCode.runner(testIO,2)).check(expectedIO)
    assert (StudentCode.runner(testIO,7)).check(expectedIO)
    assert (StudentCode.runner(testIO,13)).check(expectedIO)
    assert (StudentCode.runner(testIO,256)).check(expectedO1)
    print("Passed")
