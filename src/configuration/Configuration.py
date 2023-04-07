import yaml


class Configuration:

    def __init__(self, configuration_path):
        self.configuration_path = configuration_path

    def get_configuration(self, section):
        with open(self.configuration_path) as yml_file:
            configuration = yaml.safe_load(yml_file)

        return configuration[section]