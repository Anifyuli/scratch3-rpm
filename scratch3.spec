# RPM specfile for Scratch 3
# Maintainer: Anifyuliansyah <anifyuli007@outlook.co.id>

Name:           scratch3
Version:        3.31.1
Release:        1%{?dist}
Summary:        Scratch 3.0 as a self-contained desktop application
License:        AGPL-3.0
URL:            https://github.com/scratchfoundation/scratch-desktop
Source0:        https://github.com/scratchfoundation/scratch-desktop/archive/refs/tags/v%{version}.tar.gz
Source1:        scratch3.desktop
Source2:        scratch3-mime.xml

ExclusiveArch:  x86_64 aarch64

BuildRequires:  nodejs >= 16
BuildRequires:  npm
BuildRequires:  git-core
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  nss
BuildRequires:  gtk3
BuildRequires:  libXScrnSaver
BuildRequires:  alsa-lib
BuildRequires:  cups-libs
BuildRequires:  mesa-libgbm

Requires:       fuse-libs

%description
Scratch is coding learning platform for kids, designed, developed, and 
moderated by the Scratch Foundation. Scratch promotes computational thinking 
and problem solving skills; creative teaching and learning; self-expression 
and collaboration; and equity in computing.

NOTE: This is unofficial builds for RPM based distros

%prep
%autosetup -n scratch-desktop-%{version}

%build
# Patch: Set window icon
sed -i "s#const window = new BrowserWindow({#const window = new BrowserWindow({ icon: '/usr/share/icons/hicolor/1024x1024/apps/scratch3.png',#g" ./src/main/index.js

# Install dependencies
npm ci --legacy-peer-deps

# Build Scratch
npm run clean
npm run fetch
npm run build:dist

%install
# Install the built application
install -dm755 %{buildroot}%{_libdir}/%{name}
cp -r dist/linux-unpacked/* %{buildroot}%{_libdir}/%{name}/

# Copy electron binary if missing
if [ ! -f %{buildroot}%{_libdir}/%{name}/electron ] && [ ! -f %{buildroot}%{_libdir}/%{name}/scratch-desktop ]; then
    cp node_modules/electron/dist/electron %{buildroot}%{_libdir}/%{name}/scratch-desktop
fi

# Create launcher script
install -dm755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/bash
exec /usr/lib/scratch3/scratch-desktop "$@"
EOF
chmod 755 %{buildroot}%{_bindir}/%{name}

# Install icon
install -Dm644 src/icon/ScratchDesktop.png \
    %{buildroot}%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
install -Dm644 src/icon/ScratchDesktop.svg \
    %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Install desktop file
install -Dm644 %{SOURCE1} \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

# Install MIME types
install -Dm644 %{SOURCE2} \
    %{buildroot}%{_datadir}/mime/packages/%{name}.xml

# Install licenses
install -Dm644 LICENSE \
    %{buildroot}%{_datadir}/licenses/%{name}/LICENSE
install -Dm644 TRADEMARK \
    %{buildroot}%{_datadir}/licenses/%{name}/TRADEMARK

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/1024x1024/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml

%changelog
* Fri Dec 05 2025 Anifyuliansyah <anifyuli007@outlook.co.id> - 3.31.1-1
- Initial package
