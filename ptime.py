import time
import sys
import argparse

class PomodoroTimer():

    def __init__(self, sets_amount=3, work_min_amount=25, chill_min_amount=5) -> None:
        self.__sets = sets_amount
        self.__work_secs = work_min_amount * 60
        self.__chill_secs = chill_min_amount * 60

    def StartMainCycle(self) -> None:
        while (self.__sets > 0):
            PomodoroTimer._SetCycleWork(self, chill=False)
            PomodoroTimer._SetCycleWork(self, chill=True)
            self.__sets -= 1
        sys.stdout.write("\r\033[35mPomodoro completed!                                                      \n")

    @staticmethod
    def _SetCycleWork(self, chill=False) -> None:

        display_string = "Working"
        work_time = self.__work_secs

        if chill:
            display_string = "Chilling"
            work_time = self.__chill_secs
        

        while (work_time > 0):
            if work_time > 61:
                sys.stdout.write("\r\033[33m {}!\033[31m {:2d}\033[33m minutes remaining.".format(display_string, work_time//60))
                sys.stdout.flush()
                time.sleep(60)
                work_time -= 60
            else:
                sys.stdout.write("\r\033[32m {}!\033[31m {:2d}\033[32m seconds remaining.".format(display_string, work_time))
                sys.stdout.flush()
                time.sleep(1)
                work_time -= 1
        
        if chill:
            sys.stdout.write(f"\r\033[35mSet #{self.__sets} finished!                                                      \n")

def create_parser():
    parser = argparse.ArgumentParser(
        description="Pomodoro CLI timer",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', '--sets', 
                        required=False,
                        help="Provide number of sets u want to work:\n"
                        "Ex: python3 ptimer -s 3",
                        default=3
    )

    return parser

def main():
    try:
        parser = create_parser()
        args = parser.parse_args()
        t = PomodoroTimer(sets_amount=args.sets, work_min_amount=25, chill_min_amount=5)
        t.StartMainCycle()
    except KeyboardInterrupt:
        sys.stdout.write("\r\033[35mSet See you later!                            \n")

if __name__ == "__main__":
    sys.exit(main())