# coding=utf-8
import os
import argparse

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]
SOURCE_DIR_PATH = SCRIPT_PATH + "/.."


def test(system, args=None):
    os.chdir(SOURCE_DIR_PATH)

    # TODO: add testPresets in CMakePresets.json for different OS
    # if args.release:
    #     test_cmd = "ctest --preset " + system + "-release"
    # else:
    #     test_cmd = "ctest --preset " + system + "-debug"

    test_cmd = "ctest --test-dir build/tests/ --output-on-failure"
    print("test cmd:" + test_cmd)

    os.system(test_cmd)

    return True


def main():
    parser = argparse.ArgumentParser(description="build project")
    # parser.add_argument(
    #     "--debug", action="store_true", default=False, help="debug configuration"
    # )
    parser.add_argument(
        "--release", action="store_true", default=False, help="release configuration"
    )
    args = parser.parse_args()

    if os.name == "nt":
        system = "windows"
    elif os.name == "posix":
        system = "linux"
    else:
        print("Unsupported system: " + os.name)
        exit(1)

    if not test(system, args=args):
        exit(1)


if __name__ == "__main__":
    main()
