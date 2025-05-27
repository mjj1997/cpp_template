# coding=utf-8
import os
import argparse

SCRIPT_PATH = os.path.split(os.path.realpath(__file__))[0]
SOURCE_DIR_PATH = SCRIPT_PATH + "/.."


def pack(system, args=None):
    build_dir = SOURCE_DIR_PATH + "/build"
    os.chdir(build_dir)

    pack_cmd = "cpack"

    # TODO: different generator for different OS
    if args.zip:
        pack_cmd = "cpack -G ZIP"

    print("pack cmd:" + pack_cmd)

    os.system(pack_cmd)

    return True


def main():
    parser = argparse.ArgumentParser(description="pack project")
    parser.add_argument("--zip", action="store_true", default=False, help="pack in ZIP")
    args = parser.parse_args()

    if os.name == "nt":
        system = "windows"
    elif os.name == "posix":
        system = "linux"
    else:
        print("Unsupported system: " + os.name)
        exit(1)

    if not pack(system, args=args):
        exit(1)


if __name__ == "__main__":
    main()
