import telnetlib


class RigCtl:
    """Basic rigctl client implementation."""

    def __init__(self, hostname="127.0.0.1", port=7356):
        self.hostname = hostname
        self.port = port

    def _request(self, request):
        con = telnetlib.Telnet(self.hostname, self.port)
        con.write(("%s\n" % request).encode("ascii"))
        response = con.read_some().decode("ascii").strip()
        con.write("c\n".encode("ascii"))
        return response

    def set_frequency(self, frequency):
        return self._request("F %s" % frequency)

    def get_frequency(self):
        return self._request("f")

    def set_mode(self, mode):
        return self._request("M %s" % mode)

    def get_mode(self):
        return self._request("m")

    def get_level(self):
        return self._request("l")
