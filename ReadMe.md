# Manifest
Plugin manifest files for [iocage](https://github.com/iocage/iocage).  These files provide a convenient way to create a jail, preconfigured with some software.

## Prerequisites
A \*BSD system with the [iocage](https://github.com/iocage/iocage) jailmanager.

## Installing Plugins
Download the plugin manifest file to your local file system.

```bash
fetch https://raw.githubusercontent.com/PiESTR-TrueNAS/manifest/master/<manifest>.json
```

Install the plugin. Adjust the network settings as needed.
```bash
iocage fetch -P <manifest>.json
```

## Plugin manifest files
- [iocage-automation-n8n](https://github.com/PiESTR-TrueNAS/iocage-automation-n8n)
- [iocage-network-dyndns](https://github.com/PiESTR-TrueNAS/iocage-network-dyndns)
- [iocage-network-wireguard](https://github.com/PiESTR-TrueNAS/iocage-network-wireguard)
- [iocage-plugin-jdownloader](https://github.com/PiESTR-TrueNAS/iocage-plugin-jdownloader)
- [iocage-proxy-traefik](https://github.com/PiESTR-TrueNAS/iocage-proxy-traefik)
- [iocage-web-nginx](https://github.com/PiESTR-TrueNAS/iocage-web-nginx)
