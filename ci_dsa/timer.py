import time
import numpy as np

class timer:
    """
    Tracks timing
    """

    def __init__(self):
        self.acc = 0
        self.tic()

    def tic(self):
        """
        Starts timer

        Returns
        -------
        None.

        """
        self.t0 = time.time()

    def toc(self, restart=False):
        """
        Ends timer and calculates time

        Parameters
        ----------
        restart : bool, optional
            restart or not. The default is False.

        Returns
        -------
        diff : float
            total time taken.

        """
        diff = time.time() - self.t0
        if restart:
            self.t0 = time.time()
        return diff

    def hold(self):
        """
        Pauses timer

        Returns
        -------
        None.

        """
        self.acc += self.toc()

    def release(self):
        """
        Unpauses timer

        Returns
        -------
        ret : float
            paused time.

        """
        ret = self.acc
        self.acc = 0

        return ret

    def reset(self):
        """
        Resets timer
        """
        self.acc = 0

if __name__ == "__main__":
	start = timer()
	end = start.toc()
	print(end)
