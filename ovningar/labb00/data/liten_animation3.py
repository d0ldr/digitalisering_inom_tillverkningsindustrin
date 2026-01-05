
#!/usr/bin/env python3
import sys, time, shutil

TEXT = "  ☕ Fika kl 10:15 i köket!  "
SPEED = 0.1        # snabbare/långsammare
VARV = 1            # antal varv (hur många gånger hela texten passerar)

def main():
    try:
        sys.stdout.write("\033[?25l")  # göm cursor
        rows, cols = shutil.get_terminal_size(fallback=(24, 80))
        last_row = rows

        spacer = " " * max(cols, 1)
        marquee = TEXT + spacer
        offset = 0
        steg_per_varv = len(marquee)

        total_steg = VARV * steg_per_varv
        for _ in range(total_steg):
            # uppdatera ifall fönstret ändras
            rows, cols = shutil.get_terminal_size(fallback=(rows, cols))
            last_row = rows

            # säkerställ buffertlängd mot aktuell bredd
            if len(marquee) < len(TEXT) + cols:
                marquee = TEXT + (" " * cols)

            # bygg vy på exakt 'cols' tecken med wrap
            view = "".join(marquee[(offset + i) % len(marquee)] for i in range(cols))
            sys.stdout.write(f"\033[{last_row};1H\033[2K{view}")
            sys.stdout.flush()

            offset = (offset + 1) % len(marquee)
            time.sleep(SPEED)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h")  # visa cursor igen
        sys.stdout.write(f"\033[{shutil.get_terminal_size(fallback=(24, 80)).lines};1H\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
