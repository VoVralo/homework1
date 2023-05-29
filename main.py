import schedule

import library


def main():
    schedule.every().day.at('22:00').do(library.sleep_time)
    schedule.every().monday.at('07:00').do(library.sleep_time)
    schedule.every().tuesday.at('07:00').do(library.sleep_time)
    schedule.every().wednesday.at('07:00').do(library.sleep_time)
    schedule.every().thursday.at('07:00').do(library.sleep_time)
    schedule.every().friday.at('07:00').do(library.sleep_time)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
