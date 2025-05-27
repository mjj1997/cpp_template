# Usage

## build

1. create `vcpkg-configuration.json` and `vcpkg.json` files

```bash
vcpkg new --application
```

2. add googletest to `vcpkg.json` file

```bash
vcpkg add port gtest
```

3.  build project
- default build debug version

```bash
python scripts/build.py
```

- add `--release` to build release version

```bash
python scripts/build.py --release
```

- add `--test` to build unit tests

```bash
python scripts/build.py --test
```

- add `--example` to build examples

```bash
python scripts/build.py --example
```

## test

```bash
python scripts/test.py
```

## pack

- default pack in `tar.gz`

```bash
python scripts/pack.py
```

- add `--zip` to pack in `.zip`

```bash
python scripts/pack.py --zip
```
