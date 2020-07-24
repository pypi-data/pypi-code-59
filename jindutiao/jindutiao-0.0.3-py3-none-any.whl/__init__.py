import jindutiao
name = 'jindutiao'
def progress(length: int,
             bar: str = '#',
             delay: (float, str) = 0.01,
             **kwargs):
    jindutiao.progress(length, bar, delay, **kwargs)