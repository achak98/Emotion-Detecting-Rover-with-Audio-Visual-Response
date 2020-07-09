import argparse
import pylcd
import sys
import time

PINMAP = {
	'RS': 7,
	'E': 8,
	'D0': 25,
	'D1': 24,
	'D2': 11,
	'D3': 9,
	'D4': 10,
	'D5': 22,
	'D6': 27,
	'D7': 17,
	'CS1': 4,
	'CS2': 3,
	'RST': 2,
	'LED': 18,
}

def main():
        
        display = pylcd.ks0108.Display(backend = pylcd.GPIOBackend, pinmap = PINMAP, debug = False)
	draw = pylcd.ks0108.DisplayDraw(display)
	display.commit(full = True)
	
        sad=path of sad.png
        bored=path of bored.png
        content=path of content.png
        happy=path of happy.png
        scared=path of scared.png
        swamped=path of swamped.png
        happy2=path of happy2.png
        crying=path of crying.png
        
    while (1):
        
        val = emotionchar
        
	if val ==  Sarcasm:
            img1 = sad
            img2 = swamped
        if val == Angry:
            img1 = scared
            img2 = sad
        if val == Sad:
            img1 = sad
            img2 = crying
        if val == Fear:
            img1 = scared
            img2= crying
        if val == Bored:
            img1 = bored
            img2 = swamped
        if val == Excited:
            img1 = happy
            img2 = content
        if val== Happy:
            img1 = happy
            img2 = happy2

        display.clear()
	draw.image(img1, 0, 0, threshold = 127, angle = 0)
	display.commit()

	display.clear()
	draw.image(img2, 0, 0, threshold = 127, angle = 0)
	display.commit()
	

if __name__ == "__main__":
	main()
