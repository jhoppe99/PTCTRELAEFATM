import logging

from src.utils.args_parser import arguments_parser, get_args_from_input_file
from src.app import app

_logger = logging.getLogger(__name__)


def main():
    """Application main entry point."""
    logging.basicConfig(format="[%(asctime)s][%(name)s][%(levelname)s] - %(message)s", datefmt="%d/%m/%Y %I:%M:%S", level=logging.INFO)
    _logger.info("Hello from new ASYMTOP app!")
    args = arguments_parser()
    arguments = get_args_from_input_file(args.input_file)
    _logger.info("ARGUMENTS FROM FILE: %s", arguments)

    app(A=arguments[0], B=arguments[1], C=arguments[2], J=arguments[3])
    _logger.info("Finishing run...")

if __name__ == "__main__":
    main()
