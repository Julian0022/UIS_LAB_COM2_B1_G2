import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following:
    The block takes two values as inputs, A and Q, A is the amplitude 
    of the message, and Q is the phase of the message.
    Next, in the "work" function, the information is processed.
    Here the modulation is generated: the amplitude "A" is taken and 
    multiplied by an euler with argument "1j*Q".
    This generates a sine and cosine in which the message information is found.
    The output of this block will be the complex envelope for OOK modulation."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='e_CE_VCO_fc',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        A=input_items[0]
        Q=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(output_items[0])
        
        
