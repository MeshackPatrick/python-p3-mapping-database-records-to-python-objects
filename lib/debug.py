#!/usr/bin/env python3

from song import Song, CONN, CURSOR


def reset_database():
    Song.drop_table()
    Song.create_table()
    Song.create("Hello", "25")
    Song.create("99 Problems", "The Black Album")


if __name__ == '__main__':
    reset_database()
    import pytest; pytest.set_trace()
