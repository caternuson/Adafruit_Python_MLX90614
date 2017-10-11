# default I2C address
MLX90614_I2CADDR        = 0x5A

# RAM
MLX90614_RAWIR1         = 0x04
MLX90614_RAWIR2         = 0x05
MLX90614_TA             = 0x06
MLX90614_TOBJ1          = 0x07
MLX90614_TOBJ2          = 0x08
# EEPROM
MLX90614_TOMAX          = 0x20
MLX90614_TOMIN          = 0x21
MLX90614_PWMCTRL        = 0x22
MLX90614_TARANGE        = 0x23
MLX90614_EMISS          = 0x24
MLX90614_CONFIG         = 0x25
MLX90614_ADDR           = 0x0E
MLX90614_ID1            = 0x3C
MLX90614_ID2            = 0x3D
MLX90614_ID3            = 0x3E
MLX90614_ID4            = 0x3F

class MLX90614():
    
    def __init__(self, address=MLX90614_I2CADDR, i2c=None, **kwargs):
        if i2c is None:
            from Adafruit_GPIO import I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)
        
    def _read_temperature(self, reg):
        temp = self._device.readU16(reg)
        temp *= 0.02
        temp -= 273.15
        return temp
    
    def read_object_temperatureC(self, ):
        """Read object temperature in degrees Celcius."""
        return self._read_temperature(MLX90614_TOBJ1)   

    def read_object_temperatureF(self, ):
        """Read object temperature in degrees Fahrenheit."""
        return self.read_object_temperatureC() * (9.0/5.0) + 32.0   
    
    def read_ambient_temperatureC(self, ):
        """Read sensor temperature in degrees Celcius."""
        return self._read_temperature(MLX90614_TA)
    
    def read_ambient_temperatureF(self, ):
        """Read sensor temperature in degrees Fahrenehit."""
        return self.read_ambient_temperatureC() * (9.0/5.0) + 32.0    
