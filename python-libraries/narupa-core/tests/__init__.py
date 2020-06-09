import sys
from hypothesis import strategies as st
import numpy as np

MAX_DOUBLE = sys.float_info.max
MIN_DOUBLE = sys.float_info.min
MAX_FLOAT32 = np.finfo(np.float32).max
MIN_FLOAT32 = np.finfo(np.float32).min
MAX_UINT32 = np.iinfo(np.uint32).max

# This strategy generates a single value (i.e. not a container) that is valid
# in as value in a FrameData, and that can be safely compared with "==" (i.e.
# not numbers as ints are stored as doubles).
EXACT_SINGLE_VALUE_STRATEGY = st.one_of(
    st.text(), st.booleans(),
)

NUMBER_SINGLE_VALUE_STRATEGY = st.one_of(
    st.floats(min_value=float(MIN_DOUBLE), max_value=float(MAX_DOUBLE)),
    st.integers(min_value=int(MIN_DOUBLE), max_value=int(MAX_DOUBLE)),
)

ARRAYS_STRATEGIES = {
    'string_values': st.lists(st.text(), min_size=1),
    'index_values': st.lists(st.integers(min_value=0, max_value=MAX_UINT32), min_size=1),
    'float_values': st.lists(st.floats(min_value=float(MIN_FLOAT32), max_value=float(MAX_FLOAT32)), min_size=1),
}

MIXED_LIST_STRATEGY = st.lists(st.one_of(st.text(), st.booleans(), st.none()), min_size=1)
MIXED_DICT_STRATEGY = st.dictionaries(st.text(), st.one_of(st.text(), st.booleans(), st.none()), min_size=1)

EXACT_VALUE_STRATEGIES = st.one_of(
    MIXED_LIST_STRATEGY,
    MIXED_DICT_STRATEGY,
    EXACT_SINGLE_VALUE_STRATEGY,
)
