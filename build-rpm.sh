#!/bin/sh
VERSION=5.3.27
RPMBUILD_DIR=${HOME}/rpmbuild

mkdir -p ${RPMBUILD_DIR}
echo "Downloading slop version ${VERSION}..."
wget https://github.com/naelstrof/slop/archive/v${VERSION}.tar.gz -O ${RPMBUILD_DIR}/SOURCES/slop-${VERSION}.tar.gz

echo "Installing build dependencies..."
dnf builddep SPECS/slop.spec

echo "Building RPM..."
rpmbuild -ba SPECS/slop.spec

echo "Done! Your RPM can be found in $RPMBUILD_DIR/RPMS/{your architecture}"

