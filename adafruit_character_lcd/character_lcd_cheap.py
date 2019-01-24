import digitalio
from adafruit_character_lcd.character_lcd import Character_LCD_China

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_CharLCD.git"


class Character_LCD_Cheap(Character_LCD_China):
    def __init__(self, i2c, columns, lines, backlight_inverted=False):

        import adafruit_mcp230xx
        self._mcp = adafruit_mcp230xx.MCP23017(i2c)
        reset = self._mcp.get_pin(15)
        read_write = self._mcp.get_pin(14)
        enable = self._mcp.get_pin(13)
        db4 = self._mcp.get_pin(12)
        db5 = self._mcp.get_pin(11)
        db6 = self._mcp.get_pin(10)
        db7 = self._mcp.get_pin(9)
        red = self._mcp.get_pin(6)
        green = self._mcp.get_pin(7)
        blue = self._mcp.get_pin(8)
        self._left_button = self._mcp.get_pin(4)
        self._up_button = self._mcp.get_pin(3)
        self._down_button = self._mcp.get_pin(2)
        self._right_button = self._mcp.get_pin(1)
        self._select_button = self._mcp.get_pin(0)

        #backlight
        backlight_pin = self._mcp.get_pin(5)

        self._buttons = [self._left_button, self._up_button, self._down_button, self._right_button,
                         self._select_button]

        for pin in self._buttons:
            pin.switch_to_input(pull=digitalio.Pull.UP)

        super().__init__(reset, enable, db4, db5, db6, db7, columns, lines, red, green, blue, read_write, backlight_pin=backlight_pin, backlight_inverted=backlight_inverted)

    @property
    def left_button(self):
        return not self._left_button.value

    @property
    def up_button(self):
        return not self._up_button.value

    @property
    def down_button(self):
        return not self._down_button.value

    @property
    def right_button(self):
        return not self._right_button.value

    @property
    def select_button(self):
        return not self._select_button.value