from general.dialog import Dialog
import runpy
import os

if __name__ == '__main__':
    while True:
        class_name = input('\ninput class name =  ') + '.py'
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(root_dir, 'components', class_name)
        runpy.run_path(file_path)
        if input('Continue? (Y/N): ') == 'N':
            exit()