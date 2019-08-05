# tinder-swiper

cute little python script that automates the swiping process on tinders web client. uses the [pyautogui](https://pyautogui.readthedocs.io/en/latest/) library

# installation

In your terminal, cd to a place you want to keep this repo, and run:
```
git clone https://github.com/RyChrome/tinder-swiper.git
```

or, if you're using SSH:
```
 git@github.com:RyChrome/tinder-swiper.git
```

then, run 
```
pip install -r requirements.txt 
```

# running the script
1. in your browser, head to https://www.tinder.com, and log into your account.
2. open your terminal in the same window, and run the following:
```
python3 swiper.py
```
NOTE: the script is defaulted to swipe right 200 times. this is overboard and will probably destroy the way the algorithm rates you on the app. also, since you can only swipe right 50 times every 24 hours unless you have tinder gold, I'd suggest you change the value to something smaller like maybe 10 so you don't go OD with it.

also, if you ever find yourself in a situation where your mouse gets stuck doing some innate task like this, you can move it to the top left of the screen really quickly to have it stop the script.

happy swiping.

