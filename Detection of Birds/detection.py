from microbit import *
import microphone  

# Parameters
sample_window = 10  
threshold = 20      
detection_delay = 1000  

# Variables
samples = []
bird_count = 0

while True:
    
    reading = microphone.sound_level()
    
    
    samples.append(reading)
    if len(samples) > sample_window:
        samples.pop(0)
    
    
    mean_value = sum(samples) / len(samples)
    
    
    if abs(reading - mean_value) > threshold:
        bird_count += 1
        display.scroll(str(bird_count))
        
        display.show(Image.HEART)
        sleep(detection_delay)
    else:
        display.clear()
    
    sleep(50)  
