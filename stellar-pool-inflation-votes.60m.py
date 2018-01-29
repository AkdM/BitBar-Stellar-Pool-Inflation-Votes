#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Stellar Inflation Votes</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>AkdM</bitbar.author>
# <bitbar.author.github>akdm</bitbar.author.github>
# <bitbar.desc>Displays the number of voters for a/multiple Stellar inflation address(es)</bitbar.desc>
# <bitbar.image>https://i.imgur.com/t9bl5jd.png</bitbar.image>
#

from urllib import urlopen
import sys
import json
import subprocess

lumenaut_infl_addr = "GCCD6AJOYZCUAQLX32ZJF2MKFFAUJ53PVCFQI3RHWKL3V47QYE2BNAUT"
lumenaut_logo = "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"
xlmpool_infl_addr = "GA3FUYFOPWZ25YXTCA73RK2UGONHCO27OHQRSGV3VCE67UEPEFEDCOPA"
sdf_infl_addr = "GDWNY2POLGK65VVKIH5KQSH7VWLKRTQ5M6ADLJAYC2UEHEBEARCZJWWI"


class StellarPool:
    def __init__(self, title, infl_addr, icon=None):
        self.infl_addr    = infl_addr
        self.title        = title
        self.icon         = icon
        self.accounts     = 0
        self.votes        = 0
        self.entries      = None
        self.baseUrl      = "https://fed.network/inflation/"

        self.request()

    def render(self):
        print " {} | image={}".format(self.title, self.icon)
        print "{:,} accounts".format(self.accounts)
        print "{:,} votes".format(self.votes)

    def notify(self):
        subprocess.Popen("./usr/local/bin/terminal-notifier -title '{}' -subtitle '{:,} voters' -message '{:,} votes'".format(self.title, self.accounts, self.votes), shell=True)

    def get_inflation_votes(self):
        for voter in self.entries:
            self.votes += voter["balance"]
        self.votes = self.votes/(10**7)

    def request(self):
        url           = urlopen('{}{}'.format(self.baseUrl, self.infl_addr)).read()
        results       = json.loads(url)
        self.entries  = results["entries"]
        self.accounts = len(self.entries)
        self.get_inflation_votes()

def main(argv):
    # Stellar Logo
    print "| templateImage=iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAABmJLR0QA/wD/AP+gvaeTAAAAB3RJTUUH4gERCAY4MtZHwwAABe5JREFUOMuNlXtwVOUZxp/vO+fsjT27m72SbDaBEHIBJRFIIlARNRN0IqFQlVjANh2MKKB4aS29zJROLSoq3kBjUKEINpHajAXNxJGERAhaEMFwMTRTJJKNm2RNsmfPXs4539c/OqUTtVPf/9/f/Oadd56H4HvMkhU/xd+admHuvErMq1xEp84upatqbuHieIxvevJZPq7EeU5WJp7Y9NCVHfK/YM2HIgCAUx+/hT17d8Lh8pNXn98qlJdebTBm8CU1S/HuwYMEAAeA9Q8+OmH/O8FvHmgFAHS0d+LylwNwuZxUicVod9dhXTKZA1XVNbMKigtn2+yy6+KFC69LJnMv01NCOpkwNE3Djqe3QPwm9OEtz+Dvp3ogCGY0PP1H3HLbPWTPy8+CEMI2/Grz7YsqK9f7JnuvtdkdpqSqIny5P/l19OvNhcWFYtl1841JsgwTIRD+Azzw+m7sbXkbVQ4Jf7rwBRZNDSEl2MjB5p0UAOOyv35R1Y0NLq93mux08VC2X+MgYvhyuG9p7ep37Faz8Iu197CT3R/BbDGDvLL7jQnGZ/vDMHQdHKCyxSwNDIRTEiWzq2pq3vO43V4aH0+PxeImR1aIZ+cEhQ9a25rWrvhhLQPEFXfexfLy8xkAiEPjCmT7JKSGRxAUKOY4bGTX8DihsTH+/mPPpaAlrA1NLQ9nZuf4Y+H+5PVzSiyqqqLj5Bnm9TqRTqaUN1o74bSZ6P6/tuhmjwc//tEyEM45fLlFkGU75l5TSlw+L3yTJ3NJkgqHIsNzRkfHSurq6x4pKCokxw4fQUleiAxHR6EIAvNlZfLXXmx4aHhw8Pn82aUmye1OA8DvVt0B8f76DVizshbcZiOapsHgMClKfH1a0389FIlkXF1SgsIZM8EYUFRais/OnYXVYjWKCwuFjg86erZvfXIv1+NYXb9ODwa8IJT++91e2L0Xk6wSae88IagpXZ+eG/hJLJH6uRKL2UXCgj9bdy9CuVNFNZ6ExWICpZTbzIQc7jgS3d2463ZBkg6FsgI0M+BhALBp4wYAgHBN+XzEFZUsW1rBZKtVUJSEGpyc9cq505+0li9efvPChWVuLZFkjINoms4tFhM/feqM0tK8/4G71q5tyfFmCBlOByMgGI0OY+ENN6Kr/RDI9BkVE76i/qYMlOxrxcD+Trh63v4LL65ePnN+pW4maWq1mNJnPjtvad7XfF4f++q6xpd2DK++byMdHhpibo8XVxXlXzEmv3n8GVglgrvDW+FTB/B+7hqp6tFGfXTLslkmV+d7PXZXZo90Pyu9vo6ydByN2xu4EoslsrICt47F4u0UECglBjiw44nNVwTFHI8MALBHY9AkC36gHeLxp8o4DFbL3bbMmXkjWqBns9j1VvT0WVp0Ro1FK81W2RdXFEJFAXoi/Z1ZI6rxOFwuFy7viyH/n0D0MRlOM8AZDSCigyVlKYe5mjL6T20MFs8YjNqd2wgVlxdPy+n5KmFATKtctk+CqqoTwW6PBwDQ/fs9+IhSrNR3GjDSSJp9L/LBhFsMi119o2u2p8sV492uC7jK72zTdX2o92L/mMQI0ZMpNma3YNsffjsx3erq6lBWVgaPx0P9gQBTVTVECdUTiURYDC7EknYPUjJIRF5AQhVz2Ycjy22h7Fztw6Ptms8dAtMZHE4HFiy4dqJxQUEBMjIy6JQpU1g4HHYQQm4QBKH3zwOzwjsHa8WkfQ4Ylw1/0sQ6Go5hXfcJ1SBkQtx+frTrWzcmbW1t5Pjx47yoqMgkCMJiQki2IAgHsoLB/n9cukiy8+bzsqN+9NpX4QvHYiSJm0QiURw7coK/1rgNq+6+FzffVInVd942Edza2kouXbrEA4FAAed8OqX0HKW0v7q6Wmt6cx9W2FZC6Z8HARyEMljXffz/muy/DdLS0kIYYzYAOuc8ZTKZiM/v5xXl5QCAk59+ioHIEKxWC3TdwOfne9F99Bjypk2FLMv45SMPfhscj8fR19eHkZERcM5hsViI2WzmnHMYhoGKiorvZfjN+ReklYRrpVzEEQAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAxOC0wMS0xN1QwODowNjo1Ni0wNTowMPMtQfoAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMTgtMDEtMTdUMDg6MDY6NTYtMDU6MDCCcPlGAAAAAElFTkSuQmCC"
    print "---"
    
    # Lumenaut part
    lumenaut = StellarPool("Lumenaut", lumenaut_infl_addr, lumenaut_logo)
    lumenaut.render()

    print "---"

    # XLMPool part
    xlmPool = StellarPool("XLM Pool", xlmpool_infl_addr)
    xlmPool.render()

    print "---"
    
    # SDF part
    sdfPool = StellarPool("SDF", sdf_infl_addr)
    sdfPool.render()

    lumenaut.notify()

if __name__ == "__main__":
  main(sys.argv[1:])