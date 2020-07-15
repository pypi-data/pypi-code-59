import datetime
import enum

class FilePeriod(enum.Enum):
    
    DAILY = 86400
    HOURLY = 3600
    QUARTERLY = 900
    UNDEFINED = 0

    @staticmethod
    def from_string(string):
        """
        Get the FilePeriod from a string

        >>> FilePeriod.from_string('daily')
        FilePeriod.DAILY

        >>> FilePeriod.from_string('DAILY')
        FilePeriod.DAILY
        """

        if (string.lower() == 'daily'): return FilePeriod.DAILY
        elif (string.lower() == 'quarterly'): return FilePeriod.QUARTERLY
        elif (string.lower() == 'hourly'): return FilePeriod.HOURLY
        else: return FilePeriod.UNDEFINED

    @staticmethod
    def list():
        """ Return a list of the available valid periodicities """
        return list([v.name for v in FilePeriod if v.value > 0])

    def build_rinex3_epoch(self, epoch):
        """
        Construct a Rinex-3-like epoch string

        >>> epoch = datetime.datetime(2020, 5, 8, 9, 29, 20)
        >>> FilePeriod.QUARTERLY.build_rinex3_epoch_stream(epoch)
        '20201290915_15M'

        >>> FilePeriod.HOURLY.build_rinex3_epoch_stream(epoch)
        '20201290900_01H'

        >>> FilePeriod.DAILY.build_rinex3_epoch_stream(epoch)
        '20201290000_01D'
        """

        hour = epoch.hour if self != FilePeriod.DAILY else 0

        day_seconds = (epoch - epoch.combine(epoch, datetime.time())).total_seconds()

        minute = get_quarter_str(day_seconds) if self == FilePeriod.QUARTERLY else 0

        date_str = epoch.strftime('%Y%j')

        return '{}{:02d}{:02d}_{}'.format(date_str, hour, minute, self)


    def __str__(self):

        if self.value == FilePeriod.DAILY.value: return '01D'
        elif self.value == FilePeriod.QUARTERLY.value: return '15M'
        elif self.value == FilePeriod.HOURLY.value: return '01H'
        else:
            raise ValueError('Undefined FilePeriod value')


# ------------------------------------------------------------------------------

def get_quarter_str(seconds):
    """
    Get the Rinex quarter string ("00", "15", "30", "45") for a given number of seconds
    
    >>> get_quarter_str(100)
    0
    >>> get_quarter_str(920)
    15
    >>> get_quarter_str(1800)
    30
    >>> get_quarter_str(2900)
    45
    >>> get_quarter_str(3600 + 900)
    15
    """
    
    mod_seconds = seconds % 3600
    
    if mod_seconds < 900: return 0
    elif mod_seconds < 1800: return 15
    elif mod_seconds < 2700: return 30
    else: return 45
