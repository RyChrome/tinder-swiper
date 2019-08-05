import pyautogui


# clean code hehe xd
def click_this_many_times(number):
    for i in range(number):
        pyautogui.click(point_of_like_button)


coordinates_of_like_button = pyautogui.locateOnScreen('like.png')
point_of_like_button = pyautogui.center(coordinates_of_like_button)
click_this_many_times(200)