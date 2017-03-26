slop rpmbuild
====================

These are files for creating RPM packages for slop - well, only the spec file (that's all you need).

### How to use
(standalone - not integrated into your build system)

0. Install rpmbuild - on Fedora, this is part of the fedora-packager package
1. Clone this repository to your computer
2. Check it out to the package version you want to build for - see notes
3. Run the build-rpm.sh script
   * This will download the matching slop version into ~/rpmbuild/SOURCES
   * Runs the rpmbuild command to create an RPM

If you're doing something else, you likely already have an idea of what you need to do. You'll find the spec file in SPECS/ and you should download the matching version of slop from the slop repository (URL will be github.com/naelstrof/slop/archive/v{YOUR VERSION}.tar.gz) into your SOURCES directory.

### Notes

The release tagging on this repository roughly mirrors that of the slop repository, with the addition of a package revision number. If you're looking for the slop version that corresponds to a tag, it's the first three numbers before the "-". E.g. tag `v2.6.1-1` corresponds to slop version 2.6.1. The trailing `1` is the package revision.
