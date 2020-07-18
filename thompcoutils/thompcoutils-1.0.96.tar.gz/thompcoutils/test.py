import RPi.GPIO as GPIO
import time
import datetime

BUTTON_PIN = 16
GPIO.setmode(GPIO.BCM)


class TimedButton:
    def __init__(self, pin, callback, pull_up_down=GPIO.PUD_UP, package=None):
        """
        A TimedButton initiates a callback after a button has been pressed and then released.  It passes the duration
        the button was pressed to the callback
        :param pin: pin the button is on
        :param callback: callback to call when pressed
        :param pull_up_down: indicates the button is pulled up or down with a resistor
        :param package: package to pass to the callback
        """
        self.pin = pin
        self.package = package
        self.last_push = datetime.datetime.now()
        self.callback = callback
        self.press_time = None
        GPIO.setup(pin, GPIO.IN, pull_up_down=pull_up_down)
        GPIO.add_event_detect(pin, edge=GPIO.BOTH, callback=self._debounce_function)

    def _debounce_function(self, pin):
        """
        This function debounces the button.  Buttons are inherently noisy (they ring when pressed)  This function waits
        a period of time before declaring the button to have settled into the current state.
        :param pin: pin the button is on
        :return: None
        """
        time_now = datetime.datetime.now()
        current_state = GPIO.input(self.pin)
        if (time_now - self.last_push).microseconds > .1 * units.microseconds_per_second:
            if current_state and self.press_time is not None:
                self.callback(pin, datetime.datetime.now() - self.press_time, self.package)
            else:
                self.press_time = datetime.datetime.now()
        self.last_push = time_now

def button_callback(pin, state, argument):
    print('{} Pin {} now at {}.  Message:{}'.format(datetime.datetime.now(), pin, state, argument))

def main():
    import RPi.GPIO as GPIO
    print('Starting test_Button')
    GPIO.remove_event_detect(BUTTON_PIN)
    TimedButton(pin=BUTTON_PIN, callback=button_callback)
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()