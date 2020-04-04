""" Validates metadata submissions by extending cerberus Validator
    with field specific validators. """

import validators
import strictyaml

from cerberus import Validator
from ruamel.yaml import YAML

from dateutil.parser import ParserError, parse as dtparse

from mlspeclib.helpers import check_and_return_schema_type_by_string

class MetadataValidator(Validator):
    """ Class of all the metadata validators """

    def _validate_type_allowed_schema_types(self, value):
        """ Validates that the schema provided in the metadata file matches a
            schema provided. Returns True/False """
        return check_and_return_schema_type_by_string(value)

    def convert_and_validate(self, schema_to_check_in_text, schema_from_catalog_in_yaml):
        """ Converts text into yaml, and verifies against schema.

        schema_to_check_in_text = Text string from disk. Does validation with
                                  strictyaml and ruamel libraries, but no checking
                                  for safe strings.
        schema_from_catalog_in_yaml = Yaml already added to a SchemaCatalog from mlspeclib/data.

        Returns True/False.
        """

        strictyaml.load(schema_to_check_in_text)

        ruamel_yaml = YAML()
        parsed_proposed_yaml = ruamel_yaml.load(schema_to_check_in_text)

        self.validate(parsed_proposed_yaml, schema_from_catalog_in_yaml)
