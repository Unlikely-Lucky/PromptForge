from ..services.uninstaller import uninstall_skill


def run(args):
    uninstall_skill(args.name)