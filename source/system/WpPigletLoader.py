import os
import yaml

class WpPigletLoader:
    def __init__(self):
        None

    @staticmethod
    def load():
        piglet_path     = os.path.join(os.getcwd(),'piglets')
        piglet_listdir  = os.listdir(piglet_path)
        piglet_list     = []
    
        for piglet in piglet_listdir:
            if piglet == '__init__.py' or piglet == '__init__.pyc':
                continue
            else:
                file_path  = os.path.join(piglet_path, piglet, (str(piglet)+'.ini'))
                file = open(file_path, 'r')
                tmp_cfg        = file.read()
                file.close()

                config = yaml.load(tmp_cfg)

                piglet_list.append(config)

        return piglet_list
        