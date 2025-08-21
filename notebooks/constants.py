
from configparser import ConfigParser

constants = ConfigParser()
constants.read('../constants.ini')
constants.sections()

xi_1 = complex(constants.get('DEFAULTPARAMETERS', 'xi_1'))
xi_2 = complex(constants.get('DEFAULTPARAMETERS', 'xi_2'))
box_size = int(constants.get('DEFAULTPARAMETERS', 'box_size'))
step_x = int(constants.get('DEFAULTPARAMETERS', 'step_x'))
wp_width = float(constants.get('DEFAULTPARAMETERS', 'wp_width'))
wp_position = float(constants.get('DEFAULTPARAMETERS', 'wp_position'))
k_0 = float(constants.get('DEFAULTPARAMETERS', 'k_0'))

b_position = int(constants.get('DEFAULTPARAMETERS', 'b_position'))
b_width = int(constants.get('DEFAULTPARAMETERS', 'b_width'))
b_height = float(constants.get('DEFAULTPARAMETERS', 'b_height'))

step_t = float(constants.get('DEFAULTPARAMETERS', 'step_t'))

