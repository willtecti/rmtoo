#
# Requirement Management Toolset
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

import time
from rmtoo.lib.ReqTagGeneric import ReqTagGeneric

class ReqInventedOn(ReqTagGeneric):
    tag = "Invented on"

    def __init__(self, opts, config):
        ReqTagGeneric.__init__(self, opts, config)

    def rewrite(self, rid, req):
        # This tag (Invented on) is mandatory
        if not self.check_mandatory_tag(rid, req):
            return False, None, None

        t = req[self.tag]
        try:
            # It's better to check, if the date is ok
            pt = time.strptime(t, "%Y-%m-%d")
            del req[self.tag]
            return True, self.tag, pt
        except ValueError, ve:
            print("+++ ERROR %s: invalid date specified (must be YYYY-MM-DD) "
                  "was '%s'" % (rid, t)) 
            return False, None, None
            
