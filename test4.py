#!/usr/bin/env python
from rawsocketpy import RawSocket

sock = RawSocket("wlp2s0", 0xEEFA)
sock.send("some data")
sock.send("personal data", dest="\xAA\xBB\xCC\xDD\xEE\xFF")