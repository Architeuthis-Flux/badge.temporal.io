from pathlib import Path

from flash import (
    FACTORY_IMAGE_ASSET,
    _github_release_url,
    _release_cache_path,
    _select_release_asset,
)


def test_latest_release_url_targets_github_latest_endpoint():
    assert (
        _github_release_url("temporal-community/badge.temporal.io", "latest")
        == "https://api.github.com/repos/temporal-community/badge.temporal.io/releases/latest"
    )


def test_tagged_release_url_targets_github_tag_endpoint():
    assert (
        _github_release_url("temporal-community/badge.temporal.io", "v1.0.0")
        == "https://api.github.com/repos/temporal-community/badge.temporal.io/releases/tags/v1.0.0"
    )


def test_select_release_asset_finds_factory_image():
    asset = _select_release_asset({
        "tag_name": "v1.0.0",
        "assets": [
            {"name": "firmware.bin"},
            {"name": FACTORY_IMAGE_ASSET, "browser_download_url": "https://example.test/factory.bin"},
        ],
    })

    assert asset["name"] == FACTORY_IMAGE_ASSET


def test_select_release_asset_lists_available_assets_on_failure():
    try:
        _select_release_asset({
            "tag_name": "v1.0.0",
            "assets": [{"name": "firmware.bin"}],
        })
    except RuntimeError as exc:
        message = str(exc)
    else:
        raise AssertionError("Expected missing factory image to raise RuntimeError")

    assert FACTORY_IMAGE_ASSET in message
    assert "firmware.bin" in message


def test_release_cache_path_groups_by_tag():
    path = _release_cache_path("/tmp/replay-cache", "v1.0.0", FACTORY_IMAGE_ASSET)

    assert path == Path("/tmp/replay-cache/v1.0.0/replay2026-factory-16MB.bin")
