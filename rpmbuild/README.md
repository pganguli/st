# RPM Package

Refer to the [RPM Packaging Guide](https://rpm-packaging-guide.github.io) for more information.

# Build Instructions

```sh
rpmdev-setuptree
spectool -g -R SPECS/st.spec
rpmbuild -ba SPECS/st.spec
```

The generated package(s) can be found in `~/rpmbuild/RPMS/x86_64/`.
