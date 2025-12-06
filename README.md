# Scratch 3 Desktop - RPM Package

<div align="center">

![Scratch 3](https://scratch.mit.edu/images/scratch-og.png)

**Unofficial RPM packages for Scratch 3 Desktop on Fedora, RHEL, and derivatives**

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/anifyuli/scratch3/package/scratch3-desktop/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/anifyuli/scratch3/package/scratch3-desktop/)
[![License](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Anifyuli/scratch3-rpm)](https://github.com/Anifyuli/scratch3-rpm/issues)

[Installation](#-installation) • [Building](#-building-from-source) • [Contributing](#-contributing) • [License](#-license)

</div>

---

## 📖 About

This repository provides RPM packaging for **Scratch 3 Desktop**, the self-contained desktop application version of Scratch - a free programming language and online community where you can create your own interactive stories, games, and animations.

Scratch is developed by the Scratch Foundation and is designed to promote computational thinking and problem-solving skills, creative teaching and learning, self-expression and collaboration, and equity in computing.

> **Note**: This is an **unofficial** community package for RPM-based distributions. For official releases, visit [scratch.mit.edu](https://scratch.mit.edu/).

## ✨ Features

- 🎨 Full Scratch 3.0 desktop experience
- 🚀 Works offline - no internet required
- 📦 Native RPM packaging for Fedora/RHEL
- 🔄 Multi-architecture support (x86_64, aarch64)
- 🎯 Proper desktop integration with MIME types
- 🔒 Built from official Scratch Desktop source

## 📋 Requirements

- Fedora 41+ / RHEL 9+ / CentOS Stream 9+
- x86_64 or aarch64 architecture
- fuse-libs (for AppImage compatibility)

## 🚀 Installation

### From Copr Repository (Recommended)

```bash
# Enable the Copr repository
sudo dnf copr enable anifyuli/scratch3

# Install Scratch 3
sudo dnf install scratch3-desktop
```

### Launch Scratch 3

After installation, you can launch Scratch 3 from:
- Application menu: **Education → Scratch 3**
- Command line: `scratch3-desktop`

## 🔧 Building from Source

### Prerequisites

Install build dependencies:

```bash
sudo dnf install nodejs npm git-core rpm-build rpmdevtools \
                 desktop-file-utils libappstream-glib \
                 nss gtk3 libXScrnSaver alsa-lib cups-libs mesa-libgbm
```

### Build Steps

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Anifyuli/scratch3-rpm.git
   cd scratch3-rpm
   ```

2. **Download source tarball:**
   ```bash
   spectool -g scratch3-desktop.spec
   ```

3. **Setup RPM build environment:**
   ```bash
   rpmdev-setuptree
   cp scratch3-desktop.spec ~/rpmbuild/SPECS/
   cp *.tar.gz scratch3.desktop scratch3-mime.xml ~/rpmbuild/SOURCES/
   ```

4. **Build the RPM:**
   ```bash
   cd ~/rpmbuild/SPECS/
   rpmbuild -ba scratch3-desktop.spec
   ```

5. **Install the built package:**
   ```bash
   sudo dnf install ~/rpmbuild/RPMS/*/scratch3-*.rpm
   ```

## 📦 Package Contents

The package includes:
- Scratch 3 Desktop application
- Desktop integration files
- MIME type associations for `.sb3` and `.sprite3` files
- Application icons (PNG and SVG)
- License and trademark information

## 🐛 Known Issues

- First launch may take a few seconds to initialize
- Performance may vary on lower-end hardware

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🐛 **Report bugs** - Open an issue describing the problem
2. 💡 **Suggest features** - Share your ideas for improvements
3. 🔧 **Submit patches** - Fix bugs or add features via pull requests
4. 📝 **Improve documentation** - Help make the docs clearer

### Development Workflow

```bash
# Fork the repository
git clone https://github.com/YOUR_USERNAME/scratch3-rpm.git
cd scratch3-rpm

# Make your changes
vim scratch3-desktop.spec

# Test your changes
rpmbuild -ba scratch3-desktop.spec

# Submit a pull request
```

## 📜 License

This packaging is released under the **AGPL-3.0** license, matching the upstream Scratch Desktop license.

- Scratch Desktop: [AGPL-3.0](https://github.com/scratchfoundation/scratch-desktop/blob/develop/LICENSE)
- Packaging scripts: AGPL-3.0

## 🙏 Acknowledgments

- **Scratch Foundation** - For creating and maintaining Scratch
- **Arch Linux Community** - For the original PKGBUILD inspiration
- **Fedora Project** - For the excellent RPM packaging documentation

## 📞 Support

- 💬 **Issues**: [GitHub Issues](https://github.com/Anifyuli/scratch3-rpm/issues)
- 📧 **Email**: anifyuli007@outlook.co.id
- 🌐 **Official Scratch**: [scratch.mit.edu](https://scratch.mit.edu/)

## ⚠️ Disclaimer

This is an **unofficial community package** and is not endorsed by or affiliated with the Scratch Foundation or MIT. Scratch and the Scratch logo are trademarks of the Scratch Foundation.

For official support and downloads, please visit [scratch.mit.edu](https://scratch.mit.edu/).

---

<div align="center">

**Made with ❤️ by [Anifyuli](https://github.com/Anifyuli)**

⭐ Star this repo if you find it useful!

</div>
