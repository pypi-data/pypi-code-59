import jindutiao.jindutiao
name = 'jindutiao'
def progress(length: int,
             bar: str = '#',
             delay: (float, str) = 0.01,
             **kwargs):
    jindutiao.progress_bar(length, bar, delay, **kwargs)