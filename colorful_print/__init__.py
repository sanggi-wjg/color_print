from .printer import ColorfulPrinter

__version__ = "1.0.0"

# Default instance for convenient usage
# Users can use: from colorful_print import cp
cp = ColorfulPrinter()

# Define public API
# This helps with IDE autocomplete and explicit API declaration
__all__ = [
    "ColorfulPrinter",  # For users who want to create custom instances
    "cp",               # For users who want quick access to default instance
    "__version__",      # Version information
]
