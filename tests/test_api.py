"""Tests for vinofyi.api — API client initialization and URL construction."""

from vinofyi.api import VinoFYI


class TestVinoFYIInit:
    def test_default_base_url(self) -> None:
        client = VinoFYI()
        assert str(client._client.base_url) == "https://vinofyi.com"
        client.close()

    def test_custom_base_url(self) -> None:
        client = VinoFYI(base_url="https://staging.vinofyi.com")
        assert str(client._client.base_url) == "https://staging.vinofyi.com"
        client.close()

    def test_default_timeout(self) -> None:
        client = VinoFYI()
        assert client._client.timeout.connect == 10.0
        client.close()

    def test_custom_timeout(self) -> None:
        client = VinoFYI(timeout=30.0)
        assert client._client.timeout.connect == 30.0
        client.close()

    def test_context_manager(self) -> None:
        with VinoFYI() as api:
            assert isinstance(api, VinoFYI)
            assert not api._client.is_closed
        assert api._client.is_closed

    def test_close(self) -> None:
        client = VinoFYI()
        assert not client._client.is_closed
        client.close()
        assert client._client.is_closed


class TestVinoFYIVersion:
    def test_version(self) -> None:
        from vinofyi import __version__

        assert __version__ == "0.1.0"
