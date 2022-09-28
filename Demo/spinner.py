from halo import Halo
import time

spinner = Halo(text='Such Spins', text_color= 'cyan', color='green', spinner='dots')

try:
    spinner.start()
    time.sleep(2)
    spinner.text = 'Much Colors'
    spinner.color = 'magenta'
    spinner.text_color = 'green'
    time.sleep(2)
    spinner.text = 'Very emojis'
    spinner.spinner = 'hearts'
    spinner.text_color = 'magenta'
    time.sleep(2)
    spinner.stop_and_persist(symbol='🦄 '.encode('utf-8'), text='Wow!')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()