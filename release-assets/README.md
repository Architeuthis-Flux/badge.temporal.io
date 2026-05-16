# Release assets

Public firmware releases upload two firmware artifacts:

```text
firmware.bin
replay2026-factory-16MB.bin
```

These files are built by
[`release-firmware.yml`](../.github/workflows/release-firmware.yml) from the
`replay2026` PlatformIO environment.

`firmware.bin` is the OTA application image. The badge checks GitHub Releases
for this asset when firmware OTA is enabled.

`replay2026-factory-16MB.bin` is a complete 16 MB factory image. It includes
the bootloader, partition table, application firmware, FAT filesystem image, and
`firmware/initial_filesystem/doom1.wad`.

Recommended Ignition flash command:

```sh
cd ignition
./start.sh --latest-release
```

Ignition downloads the latest GitHub Release factory image, caches it under
`~/.cache/replay2026-badge/releases/`, and flashes it through the normal
Temporal workflow. To pin a release, use `./start.sh --release-tag v1.0.0`.
To flash a manually downloaded image, use
`./start.sh --no-build --factory-image ~/Downloads/replay2026-factory-16MB.bin`.

## Local checks

```sh
cd firmware
pio run -e replay2026
pio run -e replay2026 -t buildfs
./make_factory.sh replay2026 --no-build
```

The GitHub release workflow performs the same build and uploads
`firmware.bin` plus `replay2026-factory-16MB.bin` to the release.

## Publishing a release

`firmware/VERSION` is the source of truth for the public firmware version.
To publish a release, create and push a matching tag:

```sh
git tag v$(tr -d '[:space:]' < firmware/VERSION)
git push origin v$(tr -d '[:space:]' < firmware/VERSION)
```

Pushing a `v*` tag runs the release workflow. The workflow verifies the tag
matches `firmware/VERSION`, builds `firmware.bin`, builds
`replay2026-factory-16MB.bin`, creates or updates the GitHub Release, and
uploads both assets.

The workflow can also be run manually from GitHub Actions with an existing tag
when a release needs to be rebuilt.
