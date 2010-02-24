#
# Generic Tag Class
#
# (c) 2010 by flonatel
#
# For licencing details see COPYING
#

#
# This class is the base class of mostly all tags.
# It handles basic setup as well as handling of common cases.
#
class ReqTagGeneric:

    def __init__(self, opts, config):
        self.opts = opts
        self.config = config
        
    def type(self):
        return "reqtag"

    # Call this from the 'rewrite()' method, if the tag is mandatory.
    # Note: this function only checks the availability of the tag but
    # does not perform any other check.
    # Returns 'True' if the tag is available and 'False' if the tag is
    # not available.
    def check_mandatory_tag(self, rid, r):
        # The given tag is mandatory
        if self.tag not in r:
            print("+++ ERROR: requirement '%s' does not contain the "
                  "tag '%s'" % (rid, self.tag))
            # It's a syntax thing.
            return False
        return True

    # The method 'handle_optional_tag()' handles optional tags in the
    # sense, that it copies over the content to the class object
    # itself and removes it from the input req queue.  It does not
    # perform any other check.
    # Note: if the tag is not available, the appropritate value is set
    # to None.
    # Note: It is possible to use the return values directly from the
    # rewrite() method.
    def handle_optional_tag(self, r):
        if self.tag in r:
            v = r[self.tag]
            del r[self.tag]
            return True, self.tag, v

        return True, self.tag, None
