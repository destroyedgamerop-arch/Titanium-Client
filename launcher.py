import subprocess
import minecraft_launcher_lib

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

username = "PlayerName"
version_id = "1.21.1"

minecraft_launcher_lib.install.install_minecraft_version(
    version_id, minecraft_directory
)

options = {
    "username": username,
    "uuid": "00000000-0000-0000-0000-000000000000",
    "token": "00000000-0000-0000-0000-000000000000",
    "jvmArguments": [
        "-Xmx4G",
        "-Xms2G",
        "-XX:+UseG1GC",
        "-XX:+ParallelRefProcEnabled",
        "-XX:MaxGCPauseMillis=200",
        "-XX:+UnlockExperimentalVMOptions",
        "-XX:+DisableExplicitGC",
    ],
}

command = minecraft_launcher_lib.command.get_launch_command(
    version_id, minecraft_directory, options
)

subprocess.call(command)
