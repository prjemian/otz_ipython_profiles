"""
simulate devices
"""

__all__ = []

from ..session_logs import logger

logger.info(__file__)

import apstools.devices
import numpy

from . import calcs
from . import m1
from . import mover2
from . import registers


apstools.devices.setup_lorentzian_swait(
    calcs.calc1,
    m1.user_readback,
    center=2 * numpy.random.random() - 1,
    width=0.015 * numpy.random.random(),
    scale=10000 * (9 + numpy.random.random()),
    noise=0.05,
)

try:
    apstools.devices.setup_lorentzian_swait(
        calcs.calc2,
        mover2,
        center=2 * numpy.random.random() - 1,
        width=0.015 * numpy.random.random(),
        scale=10000 * (9 + numpy.random.random()),
        noise=0.05,
    )
    calcs.calc2.output_link_pv.put(registers.decimal1.pvname)
except NameError as exc:
    calcs.calc2.reset()
    logger.warn("reset `calc2`: %s", exc)
