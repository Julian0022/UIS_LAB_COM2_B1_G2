import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a RF VCO and works as following:
    The block takes two values as inputs, A and Q, A is
    the amplitude of the message, and Q is the phase of the message.
    Next, in the "work" function, a vector n is generated,
    this vector represents the moment of time.
    With this data, the modulation is generated: the amplitude "A" is
    taken and multiplied to a cosine with carrier frequency, and with phase "Q".
    The output of this block will be the OOK modulated signal."""

    def __init__(self, fc=128000, samp_rate=320000):  
        gr.sync_block.__init__(
            self,
            name='e_RF_VCO_ff',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.float32]
        )
        self.fc = fc
        self.samp_rate = samp_rate
        self.n_m=0

    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        n=np.linspace(self.n_m,self.n_m+N-1,N)
        self.n_m += N
        y[:]=A*np.cos(2*math.pi*self.fc*n/self.samp_rate+Q)
        return len(output_items[0])


