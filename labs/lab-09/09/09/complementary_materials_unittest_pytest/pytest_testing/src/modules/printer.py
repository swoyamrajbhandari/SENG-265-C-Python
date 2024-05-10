"""
Created on Tue Apr 26 10:36:20 2022
@author: rivera

This module allows to print output to the standard output.
"""
from sys import argv


def print_message(message: str, is_error: bool) -> None:
    """Formats a message to be printed out to the standard output.

        Parameters
        ----------
        :param message : str, required
            The message to be printed out to the standard output.

        :param is_error: bool, optional
            Indicates whether the message is an error

        Returns
        -------
        :return None
    """
    message_type: str = '[INFO]' if not is_error else '[ERROR]'
    print(f'{argv[0]} {message_type}: {message}')


def print_content_lines(title: str) -> None:
    """Creates a line to separate content.

    Parameters
    ----------
    :param title: str, required
            The title for the content

    Returns
    -------
    :return: None
    """
    print('--------------------------------------------------')
    print(f'<{title}>')
    print('--------------------------------------------------')
