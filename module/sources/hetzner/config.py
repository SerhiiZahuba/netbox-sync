from module.config import source_config_section_name
from module.config.base import ConfigBase
from module.config.option import ConfigOption


class HetznerConfig(ConfigBase):

    section_name = source_config_section_name

    def __init__(self):
        self.options = [
            ConfigOption("enabled", bool, default_value=True),
            ConfigOption("type", str),
            ConfigOption("api_token", str, mandatory=True),
        ]

        super().__init__()
