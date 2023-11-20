from pathlib import Path
from .provider import BlogProvider

__version__ = Path(__file__).joinpath('VERSION').read_text()
__all__ = ['BlogProvider']
