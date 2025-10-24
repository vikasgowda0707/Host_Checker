import unittest
import subprocess
import platform
from datetime import datetime

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", host], capture_output=True, text=True)
    return result.returncode == 0
# it will return that host is reachable or not


def load_hosts(filename = "hosts.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]
        # "r" will reads the file with will close the file after reading
        # so we use f as a refrence for opened file
        # line.strip() it removes the extra space or mewline charecter
        # for line in f it will ittirates through each line


class testNetwork(unittest.TestCase):

    def test_host_reachability(self):
        hosts = load_hosts("C:/Users/vikas/OneDrive/Desktop/network/project/hosts.txt")
        for host in hosts:
            with self.subTest(host=host): 
                # created new subset so if anyone fails it wont stop move to next
                result = ping_host(host)
                if "fake" in host:
                    self.assertFalse(result, f"{host} should not be reachable")
                else:
                    if not result:
                        self.skipTest(f"{host} is unreachable, skipping test")
                    else:
                        self.assertTrue(result, f"{host} is not reachable")


if __name__ == "__main__":
    with open("ping_test_report.txt", "w") as f:
        f.write(f"Network Ping Test Report \n Generated: {datetime.now()}\n\n")
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        unittest.main(testRunner=runner, exit=False)