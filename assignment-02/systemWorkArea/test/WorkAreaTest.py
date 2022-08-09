import os
import re
import collections
import pandas as pd
from util.FileOperationsUtil import FileOperationsUtil

class WorkAreaTest:
    def __init__(self):
        pass

    @staticmethod
    def test_work_area_coverage():
        test_name = 'WA_Test_01: Validate the work area coverage'
        print(test_name)

        tuple_lst = []

        # 1. Read points in input .txt file
        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        FileOperationsUtil.change_directory(dir, 'test', 'data')
        input_lines_lst = FileOperationsUtil.read_file('input_data/input_file.1630412935.txt')
        points_index = input_lines_lst.index('Points')
        input_points_lst = input_lines_lst[(points_index+1):]

        # 2. Read points in output .txt file
        output_points_lst = FileOperationsUtil.read_file('output_data/ouput_file.1630412935.txt')

        # 3. Determine all the output points are withing the rectangle
        # 3.1. Read rectangle coordinates
        rectangle_index = input_lines_lst.index('Rectangle')
        rectangle_points_lst = input_lines_lst[(rectangle_index + 1):(rectangle_index + 2)]
        rectangle_points_lst = rectangle_points_lst[0].split(')')
        rectangle_points_lst.pop()
        rectangle_points_lst = [re.sub("[(,]", "", rectangle_point).strip().split(' ') for rectangle_point in
                                rectangle_points_lst]

        # 3.2 Convert all lists to dataframes
        rectangle_points_df = pd.DataFrame(rectangle_points_lst, columns=['x', 'y']).astype(float)

        input_frmtd_lst = [re.sub("[()]", "", input_point).strip().split(',') for input_point in input_points_lst]
        input_points_df = pd.DataFrame(input_frmtd_lst, columns=['x', 'y']).astype(float)

        output_frmtd_lst = [re.sub("[()]", "", output_point).strip().split(',') for output_point in output_points_lst]
        output_points_df = pd.DataFrame(output_frmtd_lst, columns=['x', 'y']).astype(float)

        # 3.3 Get min and max (x, y) coordinates
        x_point_max = rectangle_points_df['x'].max()
        x_point_min = rectangle_points_df['x'].min()
        y_point_max = rectangle_points_df['y'].max()
        y_point_min = rectangle_points_df['y'].min()

        # 3.4 Check the robot has gone out of the rectangle
        invalid_points_df = output_points_df[
                (output_points_df['x'] > x_point_max) | (output_points_df['x'] < x_point_min)
                | (output_points_df['y'] > y_point_max) | (output_points_df['y'] < y_point_min)]

        if invalid_points_df.shape[0] > 0:
                print("Rectangle points: \n", rectangle_points_df)
                print("Visited points out of the rectangle: \n", invalid_points_df)
                tuple_lst = list(invalid_points_df.itertuples(index=False, name=None))

        # 4. Compare two data sets and export the test result
        # 4.1 Get valid points covered
        intersection_lst = list(set(input_points_lst) & set(output_points_lst))
        intersection_df = pd.DataFrame(intersection_lst, columns=['Expected_visiting_points'])

        # 4.2 Arrange the tuple list according to the matching format
        new_tuple_lst = []
        for x, y in tuple_lst:
                if x.is_integer():
                        x = int(x)
                if y.is_integer():
                        y = int(y)
                single_tuple = (x, y)
                new_tuple_lst.append(str(single_tuple))

        boolean_series = ~intersection_df.Expected_visiting_points.isin(new_tuple_lst)
        intersection_df = intersection_df[boolean_series]
        intersection_df['Result'] = "PASS"

        # 4.3 Get the count of occurrences for valid points
        output_points_count_dict = collections.Counter(output_points_lst)
        output_points_count_df = pd.DataFrame.from_dict(output_points_count_dict, orient='index', columns=['Count'])

        intersection_df['Count'] = None
        for rec in intersection_df['Expected_visiting_points']:
                rec_index = intersection_df[intersection_df['Expected_visiting_points'] == rec].index[0]
                intersection_df['Count'][rec_index] = output_points_count_df.filter(like=rec, axis=0).Count[0]

        # 4.4 Read miss matched points in to a dataframe
        difference_lst = list(set(input_points_lst).symmetric_difference(set(output_points_lst)))
        difference_lst = difference_lst + tuple_lst
        difference_df = pd.DataFrame(difference_lst, columns=['Not_expected_visiting_points'])
        difference_df['Result'] = "FAIL"

        # 4.5 Export test result in to a text file
        FileOperationsUtil.write_file_multiple_dfs('test_results/test_result.txt', [intersection_df, difference_df])
        # FileOperationsUtil.change_directory(dir, 'data', 'systemWorkArea')

        if difference_df.shape[0] != 0:
                return False

        return True