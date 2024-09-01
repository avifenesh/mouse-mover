import pyautogui
import threading
import keyboard
import random

exitProgram = False

screenSize = pyautogui.size()


def moveMouseRandomly():
    # Generate random coordinates within the screen boundaries
    x = random.randint(0, screenSize[0])
    y = random.randint(0, screenSize[1])

    # Move to the random position with a human-like duration
    pyautogui.moveTo(x, y, duration=random.uniform(0.5, 2.0))
    if exitProgram:
        return

    # Simulate small, precise movements
    for _ in range(random.randint(1, 3)):
        pyautogui.moveRel(
            random.randint(-10, 10),
            random.randint(-10, 10),
            duration=random.uniform(0.1, 0.3),
        )
        if exitProgram:
            return

    # Simulate scrolling
    if random.random() < 0.3:  # 30% chance to scroll
        pyautogui.scroll(random.randint(-100, 100))

    # Add random delay between movements to simulate thinking or reading
    delay = random.uniform(1.0, 5.0)
    pyautogui.sleep(delay)


def moveMouseToTopLeft():
    # Move to the top-left corner with some randomness
    x = random.randint(0, screenSize[0] // 4)
    y = random.randint(0, screenSize[1] // 4)

    pyautogui.moveTo(x, y, duration=random.uniform(0.5, 1.5))
    if exitProgram:
        return

    # Simulate small movements in the top-left area
    for _ in range(random.randint(2, 4)):
        pyautogui.moveRel(
            random.randint(-50, 50),
            random.randint(-50, 50),
            duration=random.uniform(0.2, 0.5),
        )
        if exitProgram:
            return

    # Add random delay
    delay = random.uniform(1.0, 3.0)
    pyautogui.sleep(delay)


def check_exit():
    global exitProgram
    keyboard.wait("esc")
    exitProgram = True


def main():
    global exitProgram
    exit_thread = threading.Thread(target=check_exit)
    exit_thread.start()

    while not exitProgram:
        if random.random() < 0.2:  # 20% chance to move to top-left
            top_left_thread = threading.Thread(target=moveMouseToTopLeft)
            top_left_thread.start()
            top_left_thread.join()
        else:
            random_move_thread = threading.Thread(target=moveMouseRandomly)
            random_move_thread.start()
            random_move_thread.join()

        if exitProgram:
            break


if __name__ == "__main__":
    main()
