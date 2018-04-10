

class Invalid:
    msg_fmt = _("unknown exception")

class CPUPinningUnknown(Invalid):
    msg_fmt = _("CPU set to pin/unpin %(requested)s must be a subset of "
                "known CPU set %(cpuset)s")



raise CPUPinningUnknown(requested=list(1,2,3),
                          cpuset=list(34))


