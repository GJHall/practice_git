## Graph a Sine Wave
# I made a change
import matplotlib.pyplot as plt
import numpy as np

def sine_wave():
    Fs = int(input('Sampling Rate: '))
    f = int(input('Frequency: '))
    sample = int(input('Sample Length: '))


    # Following code obtained from:
    # https://stackoverflow.com/questions/22566692/python-how-to-plot-graph-sine-wave
    # user: nikioa

    # Fs = 8000
    # f = 5
    # sample = 8000
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()

