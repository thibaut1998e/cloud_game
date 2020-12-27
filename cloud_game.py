import argparse
from main import *
import os
parser = argparse.ArgumentParser()
parser.add_argument('--location', dest='location', default=None, help='path of the level that you want to play or edit.'
                                                                      'If not provided the level is not saved. '
                                                                   'If the path do not exist it will open edition mode'
                                                                   'from scratch and save the level at this location.')

parser.add_argument('--edition-mode',  dest='edit', action='store_true', help="mode to edit your own level, the level is "
                                                                              "saved at the end")
parser.add_argument('--height', dest='height', default=500,
                    help='height of the screen, used only when creating a level from scratch')
parser.add_argument('--width', dest='width', default=1000, help='width of the screen, '
                                                                'used only when creating a level from scratch')
parser.add_argument('--speed', dest='speed', default=0.1, help='horizontal speed of the charcacter when not sprinting,'
                                                               'used only when creating a level from scratch')
parser.add_argument('--speed_sprint', dest='speed_sprint', default=0.2,
                    help='horizontal speed of the charcacter when sprinting,'
                         'used only when creating a level from scratch')
parser.add_argument('--wall-color', dest='wall_color', default='black', help='color of the walls choose among : '
                                                                           'blue, green, yellow, red, black, white')
parser.add_argument('--image', dest='image', default=default_backgroud_image,
                    help='background image path')

args = parser.parse_args()
if args.location is None or not os.path.exists(args.location):
    create_level_from_scratch(args.height, args.width, args.location,
                              args.speed, args.speed_sprint, im_path=args.image, wall_color=colors[args.wall_color])
else:
    create_game_with_file(args.location, edition_mode=args.edit, im_path=args.image, wall_color=colors[args.wall_color])





