__author__ = "Simon Nilsson", "JJ Choong"

import pandas as pd
from simba.drop_bp_cords import *
from simba.read_config_unit_tests import read_config_file
import numpy as np
from simba.misc_tools import check_multi_animal_status


class Interpolate(object):

    '''
    Class for interpolating missing body-parts in pose-estimation data

    Parameters
    ----------
    config_file_path: str
        path to SimBA project config file in Configparser format
    in_file: pd.DataFrame
        Pose-estimation data

    Notes
    -----
    `Interpolation tutorial <https://github.com/sgoldenlab/simba/blob/master/docs/Scenario1.md#to-import-multiple-dlc-csv-files>`__.

    Examples
    -----
    >>> body_part_interpolator = Interpolate(config_file_path='MyProjectConfig', in_file=input_df)
    >>> body_part_interpolator.detect_headers()
    >>> body_part_interpolator.fix_missing_values(method_str='Body-parts: Nearest')
    >>> body_part_interpolator.reorganize_headers()

    '''

    def __init__(self,
                 config_file_path: str,
                 in_file: pd.DataFrame):
        self.in_df = in_file
        config = read_config_file(ini_path=config_file_path)
        Xcols, Ycols, Pcols = getBpNames(config_file_path)
        self.columnHeaders = getBpHeaders(config_file_path)
        noAnimals = config.getint('General settings', 'animal_no')
        _, multiAnimalIDList = check_multi_animal_status(config, noAnimals)
        multiAnimalStatus = True
        self.multiAnimalIDList = [x for x in multiAnimalIDList if x]
        self.animalBpDict = create_body_part_dictionary(multiAnimalStatus, multiAnimalIDList, noAnimals, Xcols, Ycols, Pcols, [])


    def detect_headers(self):
        """
        Method to detect multi-index headers and set values to numeric in input dataframe

        Returns
        -------
        Attribute: pd.Dataframe
            current_df
        """
        self.multi_index_headers = self.in_df.iloc[0:2]
        self.multi_index_headers_list = []
        for column in self.multi_index_headers:
            self.multi_index_headers_list.append((column, self.multi_index_headers[column][0], self.multi_index_headers[column][1]))
        self.in_df.columns = self.columnHeaders
        self.current_df = self.in_df.iloc[2:].apply(pd.to_numeric).reset_index(drop=True)

    def fix_missing_values(self,
                           method_str: str):
        """
        Method to interpolate missing values in pose-estimation data.

        Parameters
        ----------
        method_str: str
            String representing interpolation method. OPTIONS: 'None','Animal(s): Nearest', 'Animal(s): Linear',
            'Animal(s): Quadratic','Body-parts: Nearest', 'Body-parts: Linear', 'Body-parts: Quadratic'

        Returns
        -------
        Attribute: pd.Dataframe
            new_df
        """

        interpolation_type, interpolation_method = method_str.split(':')[0], method_str.split(':')[1].replace(" ", "").lower()
        self.animal_df_list, self.header_list_p = [], []
        if interpolation_type == 'Animal(s)':
            for animal in self.multiAnimalIDList:
                currentAnimalX, currentAnimalY, currentAnimalP = self.animalBpDict[animal]['X_bps'], self.animalBpDict[animal]['Y_bps'], self.animalBpDict[animal]['P_bps']
                header_list_xy = []
                for col1, col2, col3, in zip(currentAnimalX, currentAnimalY, currentAnimalP):
                    header_list_xy.extend((col1, col2))
                    self.header_list_p.append(col3)
                self.animal_df_list.append(self.current_df[header_list_xy])
            for loop_val, animal_df in enumerate(self.animal_df_list):
                repeat_bol = animal_df.eq(animal_df.iloc[:, 0], axis=0).all(axis='columns')
                indices_to_replace_animal = repeat_bol.index[repeat_bol].tolist()
                print('Detected ' + str(len(indices_to_replace_animal)) + ' missing pose-estimation frames for ' + str(self.multiAnimalIDList[loop_val]) + '...')
                animal_df.loc[indices_to_replace_animal] = np.nan
                self.animal_df_list[loop_val] = animal_df.interpolate(method=interpolation_method, axis=0).ffill().bfill()
            self.new_df = pd.concat(self.animal_df_list, axis=1)


        if interpolation_type == 'Body-parts':
            for animal in self.animalBpDict:
                for x_bps_name, y_bps_name in zip(self.animalBpDict[animal]['X_bps'], self.animalBpDict[animal]['Y_bps']):
                    zero_indices = (self.current_df[(self.current_df[x_bps_name] == 0) & (self.current_df[y_bps_name] == 0)].index.tolist())
                    self.current_df.loc[zero_indices, [x_bps_name, y_bps_name]] = np.nan
                    self.current_df[x_bps_name] = self.current_df[x_bps_name].interpolate(method=interpolation_method, axis=0).ffill().bfill()
                    self.current_df[y_bps_name] = self.current_df[y_bps_name].interpolate(method=interpolation_method, axis=0).ffill().bfill()
            self.new_df = self.current_df

    def reorganize_headers(self):
        """
        Method to re-insert original multi-index headers

        Returns
        -------
        Attribute: pd.Dataframe
            new_df
        """


        loop_val = 2
        for p_col_name in self.header_list_p:
            p_col = list(self.in_df[p_col_name].iloc[2:])
            self.new_df.insert(loc=loop_val, column=p_col_name, value=p_col)
            loop_val += 3
        self.new_df.columns = pd.MultiIndex.from_tuples(self.multi_index_headers_list, names=('scorer', 'bodyparts', 'coords'))

# config_file_path = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\slp1\project_folder\project_config.ini"
# in_file = r"Z:\DeepLabCut\DLC_extract\Troubleshooting\slp1\project_folder\csv\input_csv\2020_08_01_11_27_15_857870_compressed_corrected.csv"
# interpolation_method = 'Animal(s): Quadratic'
# csv_df = pd.read_csv(in_file, index_col=0)
# #
# interpolate_body_parts = Interpolate(config_file_path, csv_df)
# interpolate_body_parts.detect_headers()
# interpolate_body_parts.fix_missing_values(interpolation_method)
# interpolate_body_parts.reorganize_headers()