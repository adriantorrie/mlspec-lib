""" Functions for validating submissions """
from distutils import util
import uritools
import semver as sv
import re


# pylint: disable=missing-class-docstring
class MLSchemaValidators:
    @staticmethod
    def validate_type_semver(value):
        """ Uses the semver library to validate Semantic Version. Returns True/False """
        return sv.VersionInfo.isvalid(value)

    # pylint: disable=invalid-name
    @staticmethod
    def validate_type_URI(value):
        """ Uses the distutils library to validate date time. Returns True/False """
        return uritools.isuri(value)

    @staticmethod
    def validate_type_path(value):
        """ Uses regex to validate the value is a path. Returns True/False """
        path_regex = re.compile("(^[a-z0-9\-._~%!$&'()*+,;=:@/]+$)")  # noqa
        return path_regex.match(value)

    @staticmethod
    def validate_type_bucket(value):
        """ Uses regex to validate the value is a path. Returns True/False """
        bucket_regex = re.compile("(?=^.{3,63}$)(?!^(\d+\.)+\d+$)(^(([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])\.)*([a-z0-9]|[a-z0-9][a-z0-9\-]*[a-z0-9])$)")  # noqa
        return bucket_regex.match(value)

    @staticmethod
    def validate_type_string_cast(value):
        """ Casts value to string and validates. Returns True/False """
        print(value)
        return isinstance(str(value), str)

    @staticmethod
    def validate_bool_and_return_string(val):
        """ Takes bool or string and converts value to string, testing
        if the result is true or false, and then casts result back to a string.

        Throws ValueError if it cannot be parsed as True/False.
        """

        # Convert to string first because some yaml libraries cast to booleans
        # and some leave as strings and we want to support both
        putative_bool_as_string = str(val)
        try:
            validated_bool = util.strtobool(putative_bool_as_string)
        except ValueError:
            raise ValueError(f"'{val}' is not a boolean value.")

        # We need to convert to 'True' or 'False' so first we cast to bool,
        # then to string.
        return str(bool(validated_bool))
