from test.WorkAreaTest import WorkAreaTest

def main():
    is_passed = WorkAreaTest.test_work_area_coverage()
    if is_passed:
        print("\n Test WA_Test_01 is Passed!")
    else:
        print("\n Test WA_Test_01 is Failed!")

if __name__ == '__main__':
    main()

