import StudentCode;
from IOWrapper import IOWrapper
testIO = IOWrapper()
expectedIO = IOWrapper()
expectedIO1 = IOWrapper()
expectedIO2 = IOWrapper()
expectedIO3 = IOWrapper()
expectedIO4= IOWrapper()

def test_hello():
    expectedIO.print("-1")
    expectedIO1.print("6")
    expectedIO2.print("3")
    expectedIO3.print("1")
    expectedIO4.print("0")
    assert (StudentCode.runner(testIO,[4, 6, 8, 10, 12, 14])).check(expectedIO)
    assert (StudentCode.runner(testIO,[-1, -2, -3, -4, -5, -6, -7])).check(expectedIO)
    assert (StudentCode.runner(testIO,[2, 3, 5, 7, 11, 13, 17])).check(expectedIO1)
    assert (StudentCode.runner(testIO,[4, 6, 8, 11, 12, 14])).check(expectedO2)
    assert (StudentCode.runner(testIO,[2, 11, 3, 5, 7, 11, 17, 11])).check(expectedO3)
    assert (StudentCode.runner(testIO,[99999989, 99999971, 99999959, 99999941, 99999931])).check(expectedO4)
    #assert (StudentCode.runner(testIO,)).check(expectedO1)
    print("Passed")
