import numpy as np
import pandas as pd
from IPython.display import display, Markdown


def page_break():  
    display(Markdown('&nbsp;'))
    display(Markdown('<style> .pagebreak { page-break-before: always; } </style><div class="pagebreak"></div>'))

def section(
    titles: 'list(str)' = [],
    subtitles: 'list(str)' = [],
    insert_break: bool = True
):  
    if insert_break:
        page_break()

    for title in titles:
        display(Markdown(f'## {title}'))

    for subtitle in subtitles:
        display(Markdown(f'#### {subtitle}'))

    display(Markdown('<hr/>'))
    
