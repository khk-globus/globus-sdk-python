import pytest

import globus_sdk


@pytest.fixture
def compute_client_v2(no_retry_transport):
    class CustomComputeClientV2(globus_sdk.ComputeClientV2):
        transport_class = no_retry_transport

    return CustomComputeClientV2()
