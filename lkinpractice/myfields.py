from typing import Any
from django.db import models
from django.core.exceptions import ValidationError

# convert hex value to integer
def hex_to_int(value):
    if value is None:
        return None
    return int(value, 16)

# convert integer value to hex
def int_to_hex(value):
    hex_val = format(value, 'X')
    # Pad with 0's
    hex_val = '0'*(6-len(hex_val)) + hex_val
    return hex_val

class RGBColorField(models.CharField):
    description = "A field for holding RGB color values"
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs['max_length'] = 6
        self._validators = []
        self.validators.append(self.validate_all_values_hex) 
        super().__init__(*args, **kwargs)
        
    def validate_all_values_hex(self, value):
        try:
            hex_to_int(value)
        except:
            raise ValidationError(f'{value} is not a hex value.')
        
    # TODO: Review this method
    def db_type(self, connection): 
        # param connection has information about which kind of database is being handled
        # why need to check the connection, because the string returned by this method could be different if the db doesn't support the command
        return 'UNSIGNED INTEGER(3)'
    
    # TODO: Review this method
    def from_db_value(self, value, expression, connection):
        if value is None:
            return None
        return int_to_hex(value)
    
    # TODO: Review this method
    def get_prep_value(self, value):
        return hex_to_int(value)