from subprocess import PIPE, Popen
from guibot.guibot import GuiBot
from pathlib import Path
import time
import sys
import pyautogui
import argparse
import webbrowser


def collect_webrtc(args, ts):
    guibot = GuiBot()

    # add path to test folder in directory
    guibot.add_path('test')

    # click webrtc stats
    # if guibot.exists('create_dump_gray.png', timeout=10):
    #     guibot.click('create_dump_gray.png')
    
    # button_location = pyautogui.locateOnScreen('test/create_dump.png')
    # print(button_location)
    # # button_center = pyautogui.center(button_location)
    # # pyautogui.click(button_center)

    # if guibot.exists('download.png', timeout=3):
    #     guibot.click('download.png')

    # save dump from webrtc
    time.sleep(10)
    res = Popen(f'mkdir webrtc', shell=True)
    res = Popen(
        f'mv ~/Downloads/webrtc_internals_dump.txt webrtc/{ts}.json', shell=True)

    # TODO: change to reflect actual args we're using
    with open('stats.log', 'a') as f:
        f.write(f'\n{ts}-{args.app}-{args.record}')

    return


def collect_traffic(args, ts):
    # _ = Popen(f'mkdir captures', shell=True)

    filename = f'captures/{ts}.pcap'

    cmd = f'tshark -i {args.interface} -w {filename} -a duration:{str(args.time)}'
    res = Popen(cmd, shell=True)
    res.wait()

    return

# launch docs
def launch_docs(args):
    # open chrome
    res = Popen('open chrome.app', shell=True)
    time.sleep(5)
    
    guibot = GuiBot()
    guibot.add_path('test')
    
    # if guibot.exists('profile.png', timeout=20):
    #     guibot.click('profile.png')


    # url = 'https://www.google.com'
    # webbrowser.get('chrome').open_new_tab(url)  
    
    # pyautogui.hotkey('command', 'n')

    pyautogui.write('chrome://webrtc-internals')
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.hotkey('command', 't')
    time.sleep(1)

    pyautogui.write("https://docs.google.com/document/d/"+args.id+"/edit")
    pyautogui.hotkey('enter')
    time.sleep(2)

    
    # if guibot.exists('google_sign_in.png', timeout=20):
    #     guibot.click('google_sign_in.png')
    #     time.sleep(2)
    #     pyautogui.write(args.email)
    #     pyautogui.press('tab')
    #     pyautogui.write(args.password)
    #     pyautogui.press('enter')
    #     time.sleep(5)

    # if guibot.exists('maximize.png', timeout=5):
    #     guibot.click('maximize.png')

    # if guibot.exists('google_docs.png', timeout=20):
    #     guibot.click('google_docs.png')
    #     time.sleep(2)

    ts = int(time.time())

    collect_traffic(args, ts)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')

    collect_webrtc(args, ts)

    pyautogui.hotkey('command', 'w')

    # if guibot.exists('google_docs_close.png', timeout=5):
    #     guibot.click('google_docs_close.png')

    return


def launch_notion(args):
    # open chrome
    res = Popen('open chrome.app', shell=True)
    time.sleep(2)
    
    guibot = GuiBot()
    guibot.add_path('test')
    
    pyautogui.write('chrome://webrtc-internals')
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.hotkey('command', 't')
    time.sleep(1)

    pyautogui.write('https://www.notion.so/kuhuhalder/'+args.id)
    pyautogui.hotkey('enter')
    time.sleep(2)
    

    # if guibot.exists('notion_sign_in.png', timeout=20):
    #     guibot.click('notion_sign_in.png')
    #     time.sleep(2)
    #     pyautogui.write(args.email)
    #     pyautogui.press('tab')
    #     pyautogui.write(args.password)
    #     pyautogui.press('enter')
    #     time.sleep(5)

    if guibot.exists('maximize.png', timeout=5):
        guibot.click('maximize.png')
        
        
    # if guibot.exists('notion_search.png', timeout=20):
    #     guibot.click('notion_search.png')
    #     time.sleep(1)
    #     pyautogui.write(args.search)
    #     pyautogui.press('enter')
        
    ts = int(time.time())

    collect_traffic(args, ts)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')

    collect_webrtc(args, ts)

    pyautogui.hotkey('command', 'w')

    return


def launch_word(args):
    pass

def launch_dropbox(args):
    # open chrome
    res = Popen('open chrome.app', shell=True)
    time.sleep(5)
    
    guibot = GuiBot()
    guibot.add_path('test')
    
    # if guibot.exists('profile.png', timeout=20):
    #     guibot.click('profile.png')


    # url = 'https://www.google.com'
    # webbrowser.get('chrome').open_new_tab(url)  
    
    # pyautogui.hotkey('command', 'n')

    pyautogui.write('chrome://webrtc-internals')
    pyautogui.press('enter')
    time.sleep(2)

    pyautogui.hotkey('command', 't')
    time.sleep(1)

    pyautogui.write("https://paper.dropbox.com/doc/"+args.id)
    pyautogui.hotkey('enter')
    time.sleep(2)


    ts = int(time.time())

    collect_traffic(args, ts)

    time.sleep(1)
    pyautogui.hotkey('ctrl', 'tab')

    collect_webrtc(args, ts)

    pyautogui.hotkey('command', 'w')

    return


def launch(args):
    if args.app == 'docs':
        launch_docs(args)
    elif args.app == 'notion':
        launch_notion(args)
    else:
        launch_dropbox(args)


def build_parser():
    parser = argparse.ArgumentParser(
        description='Launch and capture stats for document sharing')

    parser.add_argument(
        'app',
        help="Which doc sharing app to use"
    )
    parser.add_argument(
        'time',
        help="Length of sharing test"
    )
    # parser.add_argument(
    # 	'-b', '--browser',
    # 	default=False,
    # 	action='store_true',
    # 	help='Launch docs in browser (as opposed to client)'
    # )
    parser.add_argument(
        '-id', '--id',
        default ="1npeFQ8Xdj9YcVBiaKRkiOOOOjza3wJgVUSW7IRC7J6U",
        action='store',
        help='Document id'
    )

    parser.add_argument(
        '-r', '--record',
        default=None,
        action='store',
        help='Name of test to log'
    )

    parser.add_argument(
        '-i', '--interface',
        default="wlan0",
        action='store',
        help='Interface to capture network traffic'
    )

    return parser


def execute():
    parser = build_parser()
    args = parser.parse_args()

    launch(args)


if __name__ == '__main__':
    execute()
